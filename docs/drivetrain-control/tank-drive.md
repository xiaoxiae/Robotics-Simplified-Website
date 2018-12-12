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

## Implementation
Suppose that we have objects of the `Motor` class that set the speed of the motors by calling them with values from -1 to 1. We also have a `Joystick` object that returns the values of the axes `y1` and `y2`.

Implementing tank drive is really quite straightforward: simply set the left motor to whatever the `y1` axis value is, and the right motor to whatever the `y2` axis value is:

```python
def tank_drive(l_motor_speed, r_motor_speed, left_motor, right_motor):
    """Sets the speed of the left and the right motor."""
    left_motor(l_motor_speed)
    right_motor(r_motor_speed)
```

## Examples
Here's a program that makes the robot drive using the values from the joystick:

```python
# create robot's motors and the joystick
left_motor = Motor(1)
right_motor = Motor(2)
joystick = Joystick()

# continuously set motors to the values on the axes
while True:
    # get axis values
    y1 = joystick.get_y1()
    y2 = joystick.get_y2()

    # drive the robot using tank drive
    tank_drive(y1, y2, left_motor, right_motor)
```

## Closing remarks
Tank drive is a very basic and easy way to control the robot. When it comes to FRC, it is a frequently used method for its simplicity, and because it is easier for some drivers to control the robot this way, compared to the other discussed methods.
