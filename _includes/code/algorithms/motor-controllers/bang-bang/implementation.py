class Bangbang:
    """A class implementing a bang-bang controller."""

    def __init__(self, get_feedback_value):
        """Create the bang-bang controller object from the feedback function."""
        self.get_feedback_value = get_feedback_value

    def set_goal(self, goal):
        """Sets the goal of the bang-bang controller."""
        self.goal = goal

    def get_value(self):
        """Returns +1 or -1 (depending on the value of the goal) when the robot
        should be driving and 0 when it reaches the destination."""
        if self.goal > 0:
            if self.get_feedback_value() < self.goal:
                return 1    # goal not reached and is positive -> drive forward
        else:
            if self.get_feedback_value() > self.goal:
                return -1   # goal not reached and is negative -> drive backward

        # if it shouldn't be driving neither forward nor backward
        return 0