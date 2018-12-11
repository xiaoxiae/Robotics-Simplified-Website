---
layout: default
title: Tank Drive
nav_order: 1
parent: Drivetrain Control
permalink: drivetrain-control/tank-drive/
---

# Tank drive

## Introduction

Tank drive is a method of controlling the motors of a robot using two axes of a controller, where each of the axes operates motors on one side of the robot (see image below or [a video](https://www.youtube.com/watch?v=vK2CGj8gAWc)).

![Tank Drive]({{site.url}}/assets/images/drivetrain-control/tank-drive.png "Tank Drive")

---

## Implementation

Suppose that we have objects of the `Motor` class that set the speed of the motors by calling their `set(speed)` method.

We also have a `Joystick` object that returns the values of the axes `y1` and `y2`.

Implementing tank drive is really quite straight forward: simply set the left motor to whatever the `y1` axis value is, and the right motor to whatever the `y2` axis value is:

```python
def tank_drive(l_motor_speed, r_motor_speed, l_motor, r_motor):
    """Sets the speed of the left and the right motor."""
    l_motor.set(l_motor_speed)
    r_motor.set(r_motor_speed)
```

Here is sample code using our `tank_drive()` function:

```python
# create robot's motors and the joystick
l_motor = Motor(1)
r_motor = Motor(2)
joystick = Joystick()

# continuously set motors to the values on the axes
while True:
    # get axis values
    y1 = joystick.get_y1()
    y2 = joystick.get_y2()

    # drive the robot using tank drive
    tank_drive(y1, y2, l_motor, r_motor)
```

And that's it! Now you have a robot controlled with a joystick using tank drive.
