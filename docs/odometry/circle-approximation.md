---
layout: default
title: Circle Approximation
nav_order: 3
parent: Odometry
permalink: odometry/circle-approximation/
---

# Circle Approximation
Although the approximation with the assumption that the robot first turns and only then drives can be decently accurate, we can make it more precise by assuming that the robot drives in an arc (which, in reality, is quite close to what the robot is really doing), as seen on the picture bellow:

![Circle Approximation]({{site.url}}/assets/images/odometry/circle-approximation.png "Circle Approximation")

## Deriving the equations
Deriving equations for this model will be a little more difficult than the previous one, but they should still be relatively simple to follow.

The way to calculate the new coordinates is to find the radius $$R$$ of ICC ([*Instantaneous Center of Curvature*](https://en.wikipedia.org/wiki/Instant_centre_of_rotation) - the point around which the robot is turning) and then rotate $$x_0$$ and $$y_0$$ around it.


### Calculating R
Let's start by finding the formula for calculating $$R$$. We will derive it from the formulas for calculating $$l$$ and $$r$$:

$$\large l = \omega \cdot \left(R - \frac{c}{2}\right) \qquad \large r = \omega \cdot \left(R + \frac{c}{2}\right)$$

Combining the equations and solving for R gives us:

$$\large R = \left(\frac{r+l}{\omega \cdot 2} \right)$$

From our previous article about [Sensor Values]({{site.baseurl}}odometry/sensor-values/), we know that $$\omega = \frac{r - l}{c}$$. If we don't have a gyro, we can just plug that into our newly derived formula and get:

$$\large R = \frac{r+l}{\frac{r - l}{c} \cdot 2} = \frac{r+l}{r - l} \cdot \frac{c}{2}$$


### Rotating $$(x_0, y_0)$$ around ICC
For this section, we will assume that you know how to rotate a point around the origin by a certain angle. If not, here is a [video](https://www.khanacademy.org/partner-content/pixar/sets/rotation/v/sets-8) from Khan Academy deriving the equations for rotating a point around the origin.

First of, we will need the coordinates of the $$ICC$$. Since it's perpendicular to the left of the robot, we will use the same [trick](https://stackoverflow.com/questions/4780119/2d-euclidean-vector-rotations) as rotating a vector by 90 degrees counter-clockwise: switch $$x_0$$ and $$y_0$$ and negate the first coordinate:

$$\large ICC_x=x_0-R \; sin(\theta) \qquad ICC_y=y_0+R \cdot cos(\theta)$$

To rotate $$(x_0, y_0)$$ around ICC (and therefore find $$(x, y)$$), we will first translate ICC to the origin, then rotate, and then translate back:

$$\large x = (x_0 - ICC_x) \cdot cos(\omega) - (y_0 - ICC_y) \cdot sin(\omega) + ICC_x$$

$$\large y = (x_0 - ICC_x) \cdot sin(\omega) - (y_0 - ICC_y) \cdot cos(\omega) + ICC_y$$

After plugging in values for $$ICC_x$$, $$ICC_y$$ and simplifying, we get:

$$\large x = R \; sin(\theta) \cdot cos(\omega) + R \cdot cos(\theta) \cdot sin(\omega) + x_0 - R \; sin(\theta)$$

$$\large y = R \; sin(\theta) \cdot sin(\omega) - R \cdot cos(\theta) \cdot cos(\omega) + y_0 + R \; cos(\theta)$$

Using trigonometric rules, the equations can be further simplified to:

$$\large x = x_0 + R \; sin(\theta + \omega) - R \; sin(\theta)$$

$$\large y = y_0 - R \; cos(\theta + \omega) + R \; cos(\theta)$$


### Edge cases
There is one noteworthy case of values $$l$$ and $$r$$ where our circle approximation method won't work.

If $$r=l$$ (if $$\omega = 0$$), then the radius cannot be calculated, because it would be "infinite". For this reason, our method can't be used on its own, because if the robot drove in a straight line, the code would crash.

We can, however, still employ or line approximation method, since in this case, it really is driving in a straight line! It is also a good idea to apply the line approximation method for very small angles, since it's almost like driving straight, and it's far less computation-heavy.


## Implementation
Here is the implementation, combining both of the approximation methods:

```python
{% include code/algorithms/odometry/line-approximation.py %}
```