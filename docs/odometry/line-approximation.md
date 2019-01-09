---
layout: default
title: Line Approximation
nav_order: 2
parent: Odometry
permalink: odometry/line-approximation/
---

# Line Approximation
For our first approximation, let's make an assumption that will simplify our equations: instead of an arc, the robot will first turn to the specified angle, and only then drive the distance in a straight line.

This is quite a reasonable assumption to make for smaller angles, and since we are going to be updating the position multiple times per second, the angles aren't going to be as drastic as the picture portrays:

![Line Approximation]({{site.url}}/assets/images/odometry/line-approximation.png "Line Approximation")

The robot just moved a distance $$d$$. It was previously at an angle $$θ$$ and is now at an angle $$θ + ω$$. We want to calculate, what the new position of the robot is after this move.


## Deriving the equations
One of the ways to do this is to imagine a right triangle with $$d$$ being hypotenuse. We will use [trigonometric formulas](https://www2.clarku.edu/faculty/djoyce/trig/formulas.html) and solve for $$Δx$$ and $$Δy$$:

$$\large sin(\theta + \omega)=\frac{\Delta y}{d} \qquad cos(\theta + \omega)=\frac{\Delta x}{d}$$

$$\large \Delta y = d \cdot sin(\theta + \omega) \qquad \Delta x = d \cdot cos(\theta + \omega)$$

The resulting coordinates $$(x,y)$$ are $$x=x_0+Δx$$ and $$y=y_0+Δy$$.


## Implementation
Here is how one could go about implementing a class that tracks the current position of the robot by getting information from both encoders using the aforementioned line approximation methods:

```python
{% include code/algorithms/odometry/line-approximation.py %}
```

Note that for the position estimation to be accurate, the `update()` function of the class needs to be called multiple times per second.

Modified {% last_modified_at %B %-d, %Y %}
{: .fs-2 style="text-align: right;" }