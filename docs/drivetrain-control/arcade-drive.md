---
layout: default
title: Arcade Drive
nav_order: 2
parent: Drivetrain Control
permalink: drivetrain-control/arcade-drive/
---

# Arcade drive
Arcade drive is a method of controlling the motors of a robot using two axes of a controller, where one of the axes operates the "turning" component of the robot, and one the "driving" component of the robot (as if you were playing a game at an *arcade*).

![Arcade Drive]({{site.url}}/assets/images/drivetrain-control/arcade-drive.png "Arcade Drive")


## Implementation
Suppose that we have a joystick with an $$x$$ (horizontal) and a $$y$$ (vertical) axis.

There are many ways to get to the resulting arcade drive equations (for example by using [linear interpolation](https://www.chiefdelphi.com/media/papers/download/3495) for all of the 4 quadrants of the joystick input).

Here is the implementation we get by splitting the values into quadrants:

```python
{% include code/algorithms/drivetrain-control/arcade-drive/implementation.py %}
```


## Examples
Here's a program that makes the robot drive using the values from the joystick:

```python
{% include code/algorithms/drivetrain-control/arcade-drive/example.py %}
```


## Visualization
Here is a quick interactive visualization of the sorts of values our function sets the motors to for different values of $$x$$ and $$y$$:

{% include code/visualization/js/drivetrain-control/arcade-drive/visualization.js %}


## Closing remarks
If you are interested in reading more about this topic, I would suggest looking at [this thread on Chief Delphi](https://www.chiefdelphi.com/media/papers/2661), where I learned most of the information about the theory behind arcade drive.
