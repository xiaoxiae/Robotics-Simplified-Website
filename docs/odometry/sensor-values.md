---
layout: default
title: Sensor Values
nav_order: 1
parent: Odometry
permalink: odometry/sensor-values/
---

# Sensor Values
There are two things we need to know to perform the approximation:
- **Distance $$Δ$$** - how much did we move by?
- **Heading $$Δ$$** - which way are we heading?

Assuming we have encoders on both sides of the robot, the distance is quite easy to calculate: we can read the values the encoders on both of the sides are reading and average them. Assuming we also have a gyro, heading is quite easy too: we can get the heading directly as the values the gyro is returning.

But what if we didn't have a gyro?


## Calculate heading without gyro
Although gyro is arguably the most precise way to measure the current heading, it's not always available. It might be too expensive, impractical to include on a small robot, or not used because of other conditions that deem it unusable. In cases like these, it is good to know how to calculate heading only from readings of the encoders.

Say the robot drove a small arc. The left encoder measured a distance $$l$$ and the right side measured a distance $$r$$. The length between the two wheels is $$c$$, the angle by which we turned is $$ω$$ (measured in radians), and $$x$$ is just a variable to help with our calculations. Here is an illustration:

![Heading from encoders]({{site.url}}/assets/images/odometry/heading-from-encoders.png "Heading from encoders")

From this diagram, we can derive equations for the lengths of the arches $$l$$ and $$r$$ (here is an article about [arc length](https://www.mathopenref.com/arclength.html), if you need further clarification):

$$\large l=x\cdot\omega\qquad r=\left(c+x\right)\cdot\omega$$

We can then combine the equations, simplify, and solve for $$ω$$:

$$\large \frac{l}{\omega} = \frac{r}{\omega} - c$$

$$\large \omega = \frac{r - l}{c}$$

And that's it! The angle can be calculated from the difference of the readings of the encoders, divided by the length of the axis.
