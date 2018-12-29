class PID:
    """A class implementing a PID controller."""

    def __init__(self, p, i, d, get_current_time, get_feedback_value):
        """Initialises PID controller object from P, I, D constants, a function
        that returns current time and the feedback function."""
        # p, i, and d constants
        self.p, self.i, self.d = p, i, d

        # saves the functions that return the time and the feedback
        self.get_current_time = get_current_time
        self.get_feedback_value = get_feedback_value


    def reset(self):
        """Resets/creates variables for calculating the PID values."""
        # reset PID values
        self.proportional, self.integral, self.derivative = 0, 0, 0

        # reset previous time and error variables
        self.previous_time, self.previous_error = 0, 0


    def get_value(self):
        """Calculates and returns the PID value."""
        # calculate the error (how far off the goal are we)
        error = self.goal - self.get_feedback_value()

        # get current time
        time = self.get_current_time()

        # time and error differences to the previous get_value call
        delta_time = time - self.previous_time
        delta_error = error - self.previous_error

        # calculate proportional (just error times the p constant)
        self.proportional = self.p * error

        # calculate integral (error accumulated over time times the constant)
        self.integral += error * delta_time * self.i

        # calculate derivative (rate of change of the error)
        # for the rate of change, delta_time can't be 0 (divison by zero...)
        self.derivative = 0
        if delta_time > 0:
            self.derivative = delta_error / delta_time * self.d

        # update previous error and previous time values to the current values
        self.previous_time, self.previous_error = time, error

        # add past, present and future
        pid = self.proportional + self.integral + self.derivative

        # return pid adjusted to values from -1 to +1
        return 1 if pid > 1 else -1 if pid < -1 else pid


    def set_goal(self, goal):
        """Sets the goal and resets the controller variables."""
        self.goal = goal
        self.reset()
