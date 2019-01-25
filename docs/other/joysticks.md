---
layout: default
title: Joysticks
nav_order: 2
parent: Other
permalink: other/joysticks/
---

# Joysticks
![Joystick](/assets/images/other/joysticks/joystick.png "Joystick")
[Left image source](https://cdn3.volusion.com/btfzd.umflq/v/vspfiles/photos/139-2.jpg?1437257596), [Right image source](https://images-na.ssl-images-amazon.com/images/I/61F3XiCFviL._SX425_.jpg)
{: .fs-1 style="text-align: right;" }

Joysticks play a very important role in robotics competitions like FRC and FLL, as they are the single most popular way to control the robots.

Since they don't just return on/off values like keyboards do, they allow for very fine control. Another reason is that both FRC and FLL are high school competitions and video games are massively popular among teenagers, so controllers feel natural.

There are, however, some problems that need to be addressed before using them, to ensure a smooth and a pleasant user experience.


## Square to circle
![Square to circle](/assets/images/other/joysticks/square-to-circle.png "Square to circle")
[Square to circle image source](http://squircular.blogspot.com/2015/09/mapping-circle-to-square.html)
{: .fs-1 style="text-align: right;" }

When dealing with joysticks, most of us would expect that their $$x, y$$ values form a **circle**. In other words, the distance $$d$$ from origin (default controller position) is smaller than or equal to $$1$$: $$\sqrt{x^2+y^2} \le 1$$. This isn't usually the case though, as some controllers return $$x$$ and $$y$$ values from $$-1$$ to $$1$$, thus forming a **square**.

This can be a problem: suppose we're were working on a video game and we want the player to walk at a certain speed in the direction of the joystick. We would find the player running  diagonally a lot faster than vertically or horizontally. Same problems arise in robotics with swerve drive and mecanum drive control.

We need to change the $$x$$ and $$y$$ values so that their distance from origin doesn't exceed $$1$$.


### Cutting the values
The first method that comes to mind is to simply scale the values down if they are larger than 1. To do this, we will first check if $$\sqrt{x^2+y^2} \gt 1$$ and if it is, we will scale both of the coordinates down.

$$x', y' = \frac{x}{\sqrt{x^2+y^2}}, \frac{y}{\sqrt{x^2+y^2}}$$

This way is quick and easy, but the controls could feel a little weird, because there will be zones that don't react well to user input. We would ideally like to utilize all of the values, not just cut them because they are not convenient.


### Scaling by distance to the edge
Another method that would solve our problem is to find the maximum distance that the joystick could reach in the direction that it is pointing, and divide its position by this distance to scale it down so it never exceeds 1 (and we use all of the values).

The edge coordinates $$x_e$$ and $$y_e$$ can be calculated by "stretching" the current joystick values so they end up on the edge of the square. To do this, we will find the bigger of the absolute values of $$x$$ and $$y$$, and divide both the coordinates by this number.

$$x_e = \frac{x}{max(|x|, |y|)}$$

$$y_e = \frac{y}{max(|x|, |y|)}$$

Using the Pythagorean theorem, we calculate the distance to the edge of the square.

$$d_e = \sqrt{x_e^2 + y_e^2}$$

We then scale both the coordinates by this value to get the new coordinates.

$$x', y' = \frac{x}{d_e}, \frac{y}{d_e}$$

This is quite a step-up from the last method, since we are using all of the values the controller is giving us. This method also preserves the direction in which the joystick is pointing, because it only shrinks the coordinates.


### Line-ellipse method
The last method that we're going to discuss is a little heavier on math, so we aren't going to go derive the equations ourselves (they can be found [here](https://www.xarg.org/2017/07/how-to-map-a-square-to-a-circle/), including a nice visualization if you are interested). The gist of it is that to get the square, we are mapping lines of constant $$x$$ and $$y$$ onto ellipses.

$$x', y' = \left(x\sqrt{1-\frac{y^2}{2}}, y\sqrt{1-\frac{x^2}{2}}\right)$$

The coordinates that this method produces end up a little closer to what our actual value is, but it doesn't preserve the direction in which the joystick is pointing.
