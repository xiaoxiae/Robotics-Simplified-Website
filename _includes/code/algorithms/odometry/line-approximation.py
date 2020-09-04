from math import cos, sin


class LineApproximation:
    """A class to track the position of the robot in a system of coordinates
    using only encoders as feedback, using the line approximation method."""

    def __init__(self, axis_width, l_encoder, r_encoder):
        """Saves input values, initializes class variables."""
        self.axis_width = axis_width
        self.l_encoder,  self.r_encoder = l_encoder, r_encoder

        # previous values for the encoder position and heading
        self.prev_l, self.prev_r, self.prev_heading = 0, 0, 0

        # starting position of the robot
        self.x, self.y = 0, 0

    def update(self):
        """Update the position of the robot."""
        # get sensor values and the previous heading
        l, r, heading = self.l_encoder(), self.r_encoder(), self.prev_heading

        # calculate encoder deltas (differences from this and previous readings)
        l_delta, r_delta = l - self.prev_l, r - self.prev_r

        # calculate omega
        h_delta = (r_delta - l_delta) / self.axis_width

        # approximate the position using the line approximation method
        self.x += l_delta * cos(heading + h_delta)
        self.y += r_delta * sin(heading + h_delta)

        # set previous values to current values
        self.prev_l, self.prev_r, self.prev_heading = l, r, heading + h_delta

    def get_position(self):
        """Return the position of the robot."""
        return (self.x, self.y)