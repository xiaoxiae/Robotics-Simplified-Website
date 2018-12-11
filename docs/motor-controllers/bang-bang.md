---
layout: default
title: Bang-bang
nav_order: 3
parent: Motor Controllers
permalink: motor-controllers/bang-bang/
---

# Bang–bang ([wiki](https://en.wikipedia.org/wiki/Bang%E2%80%93bang_control))

## Introduction
Although our previous controller was quite easy to implement and explain, there was really not much to say about its accuracy, since there is no way for it to know, whether it really reached the target, or whether it was a few centimeters (or meters) off.

Bang-bang aims to fix this problem by using `feedback` data from our robot. Feedback data could be values from its [encoders](https://en.wikipedia.org/wiki/Encoder) (a thing that measures rotations of the wheels) or [gyro](https://en.wikipedia.org/wiki/Gyroscope) (a thing that measures where the robot is heading), or really anything else that we want to control.

---

## Implementation
The only thing the Bang-bang controller needs is the feedback function returning information about the state of whatever we're trying to control.

```python
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
```

The `get_value()` returns either `+1` or `-1` (depending on whether the goal is positive or negative) and `0` if we surpassed the goal.

This is already markedly better than our previous dead reckoning approach, but it is still relatively inaccurate, thanks to robot's inertia when the controller tells it to stop driving.

We could try to fix this by saying that once it passes the goal, it should start driving back, but the only thing you'd get is a robot that drives back and forward across the goal.
