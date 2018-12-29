from math import cos, sin

class CircleApproximation:
    """A class to track the position of the robot in a system of coordinates
    using only encoders as feedback, using a combination of line and circle
    approximation methods."""

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

        # calculate ω
        h_delta = (r_delta - l_delta) / self.axis_width

        # either approximate if we're going (almost) straight or calculate arc
        if abs(l_delta - r_delta) < 1e-5:
            self.x += l_delta * cos(heading)
            self.y += r_delta * sin(heading)
        else:
            # calculate the radius of ICC
            R = (self.axis_width / 2) * (r_delta + l_delta) / (r_delta - l_delta)

            # calculate the robot position by finding a point that is rotated
            # around ICC by heading delta
            self.x +=   R * sin(h_delta + heading) - R * sin(heading)
            self.y += - R * cos(h_delta + heading) + R * cos(heading)

        # set previous values to current values
        self.prev_l, self.prev_r, self.prev_heading = l, r, heading + h_delta


    def get_position(self):
        """Return the position of the robot."""
        return (self.x, self.y)