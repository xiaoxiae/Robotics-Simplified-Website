---
layout: default
title: Line Approximation
nav_order: 2
parent: Odometry
permalink: odometry/line-approximation/
---

# Line Approximation
For our first approximation, let's make an assumption: instead of driving an arc, the robot will first turn by the specified angle, and only then drive the distance in a straight line.

This is quite a reasonable assumption to make for smaller angles: since we are updating the position multiple times per second, the angles aren't going to be too large.

![Line Approximation]({{site.url}}/assets/images/odometry/line-approximation.png "Line Approximation")

## Deriving the equations
The robot moved a distance $$d$$. It was previously at an angle $$\theta$$ and is now at an angle $$\theta + \omega$$. We want to calculate, what the new position of the robot is after this move.

One of the ways to do this is to imagine a right triangle with $$d$$ being hypotenuse. We will use [trigonometric formulas](https://www2.clarku.edu/faculty/djoyce/trig/formulas.html) and solve for $$\Delta x$$ and $$\Delta y$$:

$$sin(\theta + \omega)=\frac{\Delta y}{d} \qquad cos(\theta + \omega)=\frac{\Delta x}{d}$$

$$\Delta y = d \cdot sin(\theta + \omega) \qquad \Delta x = d \cdot cos(\theta + \omega)$$

The resulting coordinates $$(x,y)$$ are $$x=x_0+\Delta x$$ and $$y=y_0+\Delta y$$.


## Implementation
This is one of the possible implementations of a class that tracks the current position of the robot by getting information from both encoders using the aforementioned line approximation method.

Note that for the position estimation to be accurate, the `update()` function of the class needs to be called multiple times per second.

```python
{% include code/algorithms/odometry/line-approximation.py %}
```

Modified {% last_modified_at %B %-d, %Y %}
{: .fs-2 style="text-align: right;" }
