---
layout: default
title: Sensor Values
nav_order: 1
parent: Odometry
permalink: odometry/sensor-values/
---

# Sensor Values
Let's talk about information that we will need for calculating our current position (`x` and `y` coordinates on a grid, starting at `(0, 0)`).

The two main ones are:
- **Driven distance** - what is the distance driven by the wheels of the robot.
- **Heading** - which way is the robot pointing?

The former is quite easy: we can simply check the values of the encoders that our robot has on each of the sides. With gyro,


## Calculate heading without gyro
Although gyro is arguably the best way to measure the current heading, it's not always available. In cases that you can't use gyro, it is helpful to know, how to calculate heading from the values of the encoders.

Say the robot drove a small arc. The left encoder measured a distance `l` and the right side measured a distance `r`. The length between the two wheels is `c`, the angle by which we turned is `ω` (measured in radians), and `x` is just a variable to help with our calculations. Here is an illustration:

![Heading from encoders]({{site.url}}/assets/images/odometry/heading-from-encoders.png "Heading from encoders")

From this diagram, we can derive equations for the lengths of the arches `l` and `r` (here is an article about [arc length](https://www.mathopenref.com/arclength.html), if you need further clarification):

![](http://mathurl.com/yaj68z7t.png)
{: .text-center }

We can then combine the equations, simplify, and solve for `ω`:

![](http://mathurl.com/yan8lkvg.png)
{: .text-center }

![](http://mathurl.com/ydbzpnfo.png)
{: .text-center }

And that's it! The angle can be calculated from the difference of the readings of the encoders, divided by the length of the axis.
