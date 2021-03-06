---
layout: default
title: Polynomial Function
nav_order: 5
parent: Motor Controllers
permalink: motor-controllers/polynomial-function/
---

# Polynomial Function
Another way that we can get values that aren't just 1's and 0's is to model a function from points and get the speed of the robot from it -- for example: let's say that we start at speed 0.2, drive at full speed when we're at half the distance and slow down to 0 when we're at the end.

Polynomial function is a great candidate for this task. We can pick points that we want the function to pass through and then use [polynomial regression](https://en.wikipedia.org/wiki/Polynomial_regression) to get the coefficients of the function.

![Polynomial function]({{site.baseurl}}/assets/images/motor-controllers/polynomial-function.png "Polynomial function")

One thing you should also notice is that the function starts at $$x = 0$$ and ends at $$x = 1$$. This is deliberate -- it makes it easy for us to "stretch" the function a little wider if we want to drive some other distance, not just a distance of 1.


## Horner's method
When it comes to programming, exponentiation tends to be quite expensive. [Horner's method](https://en.wikipedia.org/wiki/Horner%27s_method) is an elegant solution to this problem. The concept is simple -- change the expression by repeatedly taking out $$x$$, so there is no exponentiation.

$$2x^3 + 4x^2 -x + 5 \quad \rightarrow \quad x(x(x(2) + 4) - 1) + 5$$

This requires fewer multiplications, thus making the evaluation faster.


## Implementation
The controller only needs the coefficients of the polynomial that we modeled, and a feedback function.

```python
{% include code/algorithms/motor-controllers/polynomial-function/implementation.py %}
```


## Examples

### Driving a distance
Once again, the code is almost the exact same as the examples from nearly all of the other controllers.

```python
{% include code/algorithms/motor-controllers/polynomial-function/example.py %}
```


## Generating a polynomial
An alternative to "stretching" the polynomial to fit the goal is to specify the points the polynomial passes through and generate the coefficients *after* the goal is specified.

Say you have points $$\left(0,0.2\right)$$, $$\left(0.4,1\right)$$, $$\left(0.6,1\right)$$ and $$\left(1,0\right)$$. Since there are 4 points, the general form of the polynomial is $$y=ax^3+bx^2+cx+d$$ Using this information, we can create a system of linear equations:

$$\begin{array}{rcl}
0.2 & = & a(0)^3+b(0)^2+c(0)+d \\
1   & = & a(0.4)^3+b(0.4)^2+c(0.4)+d \\
1   & = & a(0.6)^3+b(0.6)^2+c(0.6)+d \\
0   & = & a(1)^3+b(1)^2+c(1)+d
\end{array}$$

Solving this system of linear equations will give us the coefficients of the polynomial. We can apply this method to a polynomial of any degree $$d$$, if we have at least $$d+1$$ number of points.


## Closing remarks
Although this controller isn't as widely used as PID, it can sometimes outperform PID, namely in situations where the ranges of movement of the motors are restricted -- forks of a forklift/robot arm.
