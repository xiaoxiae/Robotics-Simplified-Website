---
layout: default
title: Polynomial Function
nav_order: 5
parent: Motor Controllers
permalink: motor-controllers/polynomial-function/
---

# Polynomial Function

## Introduction
Another way that we can get values that aren't just 1's and 0's is to model a function from points and get the speed of the robot from it - for example: let's say that we start at speed 0.2, drive at full speed when we're at half the distance and slow down to 0 when we're at the end.

Polynomial function is a great candidate for this task. We can pick points that we want the function to pass through and then use [polynomial regression](https://en.wikipedia.org/wiki/Polynomial_regression) to get the coefficients of the function. [MyCurveFit.com](https://mycurvefit.com/) is a great website to use for this exact purpose. Here is how a modeled polynomial function could look like:

![Polynomial function]({{site.url}}/assets/images/motor-controllers/polynomial-function.png "Polynomial function")

As you can see, it returns all sorts of values from 0 to 1.

One thing you should also notice is that the function starts at `x = 0` and ends at `x = 1`. This is deliberate - it makes it easy for us to "stretch" the function a little wider if we want to drive some other distance.


## [Horner's method](https://en.wikipedia.org/wiki/Horner%27s_method)
When it comes to programming, exponentiation tends to be quite imprecise and slow. Horner's method is a neat solution to this problem. The concept is simple - change the expression so there is no exponentiation (only multiplication and addition) using algebraic operations:


$$\large 2x^3 + 4x^2 -x + 5 \quad \rightarrow \quad x(x(x(2) + 4) - 1) + 5$$

This trick can be performed on a polynomial of any size, this is just an example of how the method works.


## Implementation
The controller only needs the coefficients of the polynomial that we modeled, and a feedback function. Here is how the implementation would look like with Horner's method:

```python
class PolynomialFunction:
    """A class implementing a polynomial function controller."""

    def __init__(self, coefficients, get_feedback_value):
        """Initialises the polynomial function controller from the polynomial
        coefficients and the feedback value."""
        self.coefficients = coefficients    # the coefficients of the function
        self.get_feedback_value = get_feedback_value   # the feedback function


    def get_value(self):
        """Returns the polynomial function value at feedback function value."""
        # calculate the x coordinate (by "stretching" the function by goal)
        x = self.get_feedback_value() / abs(self.goal)

        # calculate function value using Horner's method
        value = self.coefficients[0]
        for i in range(1, len(self.coefficients)):
            value = x * value + self.coefficients[i]

        # if the value is over 1, set it to 1
        if value > 1:
            value = 1

        # if goal is negative, function value is negative
        return value if self.goal > 0 else -value


    def set_goal(self, goal):
        """Sets the goal of the controller."""
        self.goal = goal
```


## Examples

### Driving a distance
Once again, the code is almost the exact same as the examples from nearly all of the other controllers, the only difference is that a `PolynomialFunction` controller takes a list of coefficients of the polynomial to calculate the controller value, compared to the inputs of other controllers:

```python
# create robot's motors, gyro and the encoder
left_motor = Motor(1)
right_motor = Motor(2)
encoder = Encoder()

# create the controller (with encoder as the feedback function)
controller = PolynomialFunction([-15.69, 30.56, -21.97, 6.91, 0.2], encoder)
controller.set_goal(10)

while True:
    # get the speed from the controller and apply it using tank drive
    value = controller.get_value()
    tank_drive(value, value, left_motor, right_motor)
```
