---
layout: default
title: PID
nav_order: 4
parent: Motor Controllers
permalink: motor-controllers/pid/
---

# PID ([wiki](https://en.wikipedia.org/wiki/PID_controller))

## Introduction
Our previous attempt at creating a controller that used feedback from the robot could be further improved by considering how the feedback value that the robot returns changes over time.

Let's introduce a new term called **error.** Error is the feedback value minus the goal and tells us, how far off we are from the goal.

Let's break down that the terms **P**, **I** and **D** mean in our PID controller using our newly defined error:
- **P** stands for proportional - how big is the error now (in the **present**).
- **I** stands for integral - how big the error was (the previous errors accumulated) in the **past.**
- **D** stands for derivative - what will the error likely be in the **future.**

The controller takes into account what happened, what is happening now, and what will likely happen and produces a value based on that information.

To do this, it will need a few extra sources of information (compared to bang-bang and dead reckoning), namely `p`, `i` and `d` constants that will tell the controller, how important are each of the aforementioned parts (proportional, integral, derivative).

## Implementation
Besides the constants, the controller will also obviously need the feedback function, and, to correctly calculate the integral and derivative, a function that returns the current time:

```python
class PID:
    """A class implementing a PID controller."""

    def __init__(self, p, i, d, get_current_time, get_feedback_value):
        """Initialises PID controller object from P, I, D constants, a function
        that returns current time and the feedback function."""
        # p, i, and d constants
        self.p, self.i, self.d = p, i, d

        # saves the functions that return the time and the feedback
        self.get_current_time = get_current_time
        self.get_feedback_value = get_feedback_value


    def reset(self):
        """Resets/creates variables for calculating the PID values."""
        # reset PID values
        self.proportional, self.integral, self.derivative = 0, 0, 0

        # reset previous time and error variables
        self.previous_time, self.previous_error = 0, 0


    def get_value(self):
        """Calculates and returns the PID value."""
        # calculate the error (how far off the goal are we)
        error = self.goal - self.get_feedback_value()

        # get current time
        time = self.get_current_time()

        # time and error differences to the previous get_value call
        delta_time = time - self.previous_time
        delta_error = error - self.previous_error

        # calculate proportional and integral
        self.proportional = self.p * error
        self.integral += error * delta_time * self.i

        # if time delta isn't zero, calculate derivative
        self.derivative = 0
        if delta_time > 0:
            self.derivative = delta_error / delta_time * self.d

        # update previous_error and previous_time values to the current values
        self.previous_time, self.previous_error = time, error

        # return the PID value (adjusted to [-1; 1])
        pid = self.proportional + self.integral + self.derivative
        return 1 if pid > 1 else -1 if pid < -1 else pid


    def set_goal(self, goal):
        """Sets the goal and resets the controller variables."""
        self.goal = goal
        self.reset()
```

## Configuring the controller
PID is the first discussed controller that actually needs to be configured properly to function well (there is a [whole section](https://en.wikipedia.org/wiki/PID_controller#Loop_tuning) on Wikipedia), because if you give wrong constants to the controller, it will start to behave unpredictably.

We won't go into details of how, but it is just something to keep in mind when programming a robot's movement using this type of controller.

## Examples

### Driving distance
Here is the first example that makes the robot drive 10 meters forward. The constants are sample values that I used on the Vex EDR robot that I built to test the PID code:

```python
# create robot's motors, gyro and the encoder
left_motor = Motor(1)
right_motor = Motor(2)
encoder = Encoder()

# create the PID controller with encoder being the feedback function
controller = PID(0.07, 0.001, 0.002, time, encoder)

controller.set_goal(10)

while True:
    # get the controller value and set it on both motors
    value = controller.get_value()
    tank_drive(value, value, left_motor, right_motor)
```

### Auto-correcting robot
Another problem that we could solve using PID is a self-correcting robot - a robot that stays in one place and continuously corrects its heading when bumped. For this, we will need a `Gyro` class, whose object will give us the current heading of the robot when called.

One thing we have to think about is what to set the motors to when we get the value from the controller. Luckily, `arcade_drive` will be our savior: we can plug our PID values directly into the turning part of arcade drive (the `x` axis) to steer the robot:

```python
# create robot's motors and the gyro
left_motor = Motor(1)
right_motor = Motor(2)
gyro = Gyro()

# create the PID controller with gyro being the feedback function
controller = PID(0.2, 0.002, 0.015, time, gyro)

# we want to stay at the 0° angle
controller.set_goal(0)

while True:
    # set the turning component of arcade drive to controller value
    arcade_drive(controller.get_value(), 0, left_motor, right_motor)
```

### Auto-correcting driving robot
What's even nicer is that we can combine the two examples that we just implemented into ONE - a robot that drives forward and corrects itself when it isn't heading the right way:

We will create two controllers - one for driving straight by a certain distance and one for turning to correct possible heading errors.

Arcade drive will again be our dear friend, since we can plug values from the controller that controls driving directly into the driving part of arcade drive, and the controller that controls turning directly into the turning part of arcade drive:

```python
# create robot's motors, gyro and the encoder
left_motor = Motor(1)
right_motor = Motor(2)
gyro = Gyro()
encoder = Encoder()

# create the PID controller with gyro being the feedback function
drive_controller = PID(0.07, 0.001, 0.002, time, encoder)
turn_controller = PID(0.2, 0.002, 0.015, time, gyro)

# we want to stay at the 0° angle and drive 10 meters
turn_controller.set_goal(0)
drive_controller.set_goal(10)

while True:
    # get the values from both controllers
    turn_value = turn_controller.get_value()
    drive_value = drive_controller.get_value()

    # drive/turn using arcade drive
    arcade_drive(turn_value, drive_value, left_motor, right_motor)
```
