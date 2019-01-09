---
layout: default
title: Tank Drive
nav_order: 1
parent: Drivetrain Control
permalink: drivetrain-control/tank-drive/
---

# Tank drive
Tank drive is a method of controlling the motors of a robot using two axes of a controller, where each of the axes operates motors on one side of the robot (see image below or [a video](https://www.youtube.com/watch?v=vK2CGj8gAWc)).

![Tank Drive]({{site.url}}/assets/images/drivetrain-control/tank-drive.png "Tank Drive")

[Robot CAD model](https://grabcad.com/library/wild-thumper-6wd-chassis-1), [Controller image source](https://target.scene7.com/is/image/Target/GUEST_1e4c1fcb-6962-4533-b961-4e760355db27?wid=488&hei=488&fmt=pjpeg)
{: .fs-1 style="text-align: right;" }


## Implementation
Suppose that we have objects of the `Motor` class that set the speed of the motors by calling them with values from -1 to 1. We also have a `Joystick` object that returns the values of the axes $$y_1$$ and $$y_2$$.

Implementing tank drive is really quite straightforward: simply set the left motor to whatever the $$y_1$$ axis value is, and the right motor to whatever the $$y_2$$ axis value is:

```python
{% include code/algorithms/drivetrain-control/tank-drive/implementation.py %}
```


## Examples
Here's a program that makes the robot drive using the values from the joystick:

```python
{% include code/algorithms/drivetrain-control/tank-drive/example.py %}
```


## Closing remarks
Tank drive is a very basic and easy way to control the robot. When it comes to FRC, it is a frequently used method for its simplicity, and because it is easier for some drivers to control the robot this way, compared to the other discussed methods.

Modified {% last_modified_at %B %-d, %Y %}
{: .fs-2 style="text-align: right;" }