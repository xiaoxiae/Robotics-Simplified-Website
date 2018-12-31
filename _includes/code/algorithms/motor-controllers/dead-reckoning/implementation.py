class DeadReckoning:
    """A class implementing a dead reckoning controller."""

    def __init__(self, speed, get_current_time):
        """Takes the average speed and a function that returns current time."""
        self.get_current_time = get_current_time
        self.speed = speed


    def set_goal(self, goal):
        """Sets the goal of the controller (and also starts the controller)."""
        self.goal = goal
        self.start_time = self.get_current_time()


    def get_value(self):
        """Return the current value the controller is returning."""
        # at what time should we reach the destination (d=d_0 + s/v)
        arrival_time = self.start_time + (self.goal / self.speed)

        # return +-1 if we should have reached the destination and 0 if not
        if self.get_current_time() < arrival_time:
            return 1 if self.goal > 0 else -1
        else:
            return 0