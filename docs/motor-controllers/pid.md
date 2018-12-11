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

Let's introduce a new term called **error.** Error is the current feedback value minus the previous feedback value. It essentially tells us, how far off we are from the goal.

With error in mind, let's break down that the terms **P**, **I** and **D** mean in our PID controller:
- **P** stands for proportional - how big is the error now (in the **present**).
- **I** stands for integral - how big the error was (accumulatively) in the **past.**
- **D** stands for derivative - what will the error likely be in the **future.**

The controller takes into account what happened, what is happening now, and what will likely happen and produces a value based on that information. To do this, it needs a few extra things compared to Bang-bang, namely **PID constants**: values that tell the controller, how important is each of the parts (past, present, future).

## Implementation

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
        self.previous_time = time
        self.previous_error = error

        # return the PID value (adjusted to the range [-1; 1])
        pid = self.proportional + self.integral + self.derivative
        return 1 if pid > 1 else -1 if pid < -1 else pid


    def set_goal(self, goal):
        """Sets the goal and resets the controller variables."""
        self.goal = goal
        self.reset()
```

## Configuring the controller
PID is the very first controller that actually needs to be configured properly to function well (there is a [whole section](https://en.wikipedia.org/wiki/PID_controller#Loop_tuning) on Wikipedia), because if you give wrong constants to the controller, it will start to behave weirdly.
