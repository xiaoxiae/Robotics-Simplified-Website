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
