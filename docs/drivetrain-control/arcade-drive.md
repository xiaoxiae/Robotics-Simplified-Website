---
layout: default
title: Arcade Drive
nav_order: 2
parent: Drivetrain Control
permalink: drivetrain-control/arcade-drive/
---

# Arcade drive
Arcade drive is a method of controlling the motors of a _tank drive drivetrain_ using two axes of a controller, where one of the axes controls the speed of the robot, and the other the steering of the robot.

![Arcade Drive]({{site.url}}/assets/images/drivetrain-control/arcade-drive.png "Arcade Drive")

[Robot CAD model](https://grabcad.com/library/wild-thumper-6wd-chassis-1), [Controller image source](https://target.scene7.com/is/image/Target/GUEST_1e4c1fcb-6962-4533-b961-4e760355db27?wid=488&hei=488&fmt=pjpeg)
{: .fs-1 style="text-align: right;" }


## Deriving the equations
The equations used in the implementation are derived using [linear interpolation](https://en.wikipedia.org/wiki/Linear_interpolation). This allows us to transition from one coordinate to the other in a linear fashion, which provides a pleasant driving experience.

I won't show the derivation here, since it isn't too exciting (if you're interested, it can be found in [this post](https://www.chiefdelphi.com/t/paper-arcade-drive/168720) on Chief Delphi), but rather an illustration to help you understand the derivation more intuitively.

![Arcade Drive Illustration]({{site.url}}/assets/images/drivetrain-control/arcade-drive-illustration.png "Arcade Drive Illustration")

What we want is to transform our $$x$$ and $$y$$ coordinates to the speeds of the motor. To do this, let's focus on the values we would *like* to be getting in the 1st quadrant. The left rectangle in the illustration represents the joystick values (in the 1st quadrant) and right one the speeds of the left and right motor (in the 1st quadrant). I would suggest you see the visualization at the end of the article, it demonstrates this nicely.

The speeds of the left motor $$l$$ are $$1$$ in all of the corners (besides the origin). Using $$x, y$$, we can achieve the same values by saying that $$l$$ is the bigger of the two... $$l = \text{max}(x, y)$$.

As for the right motor $$r$$, As the $$x$$ and $$y$$ change their values, $$r$$ goes from $$1$$ (top left) to $$-1$$ (bottom right). We can model the same values using difference... $$r = y - x$$.

A similar observation can be made about the other quadrants. This is mostly to show that you can think about the derivations more intuitively (since this particular one it isn't too complicated).


## Implementation
```python
{% include code/algorithms/drivetrain-control/arcade-drive/implementation.py %}
```


## Examples
The following example demonstrates, how to make the robot drive using arcade drive controlled by a joystick.

```python
{% include code/algorithms/drivetrain-control/arcade-drive/example.py %}
```


## Visualization
Here is an interactive visualization of the sorts of values our function sets the motors to for different values of $$x$$ and $$y$$:

{% include code/visualization/js/drivetrain-control/arcade-drive/visualization.js %}


## Closing remarks
If you are interested in reading more about this topic, I would suggest looking at [this thread on Chief Delphi](https://www.chiefdelphi.com/media/papers/2661), where I learned most of the information about the theory behind arcade drive.

Modified {% last_modified_at %B %-d, %Y %}
{: .fs-2 style="text-align: right;" }