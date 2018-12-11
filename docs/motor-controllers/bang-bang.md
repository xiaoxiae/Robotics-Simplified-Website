---
layout: default
title: Bang-bang
nav_order: 3
parent: Motor Controllers
permalink: motor-controllers/bang-bang/
---

# Bang–bang ([wiki](https://en.wikipedia.org/wiki/Bang%E2%80%93bang_control))

## Introduction
Although our previous controller was quite easy to implement and explain, there is no way for it to know, whether it reached the target or not.

Bang-bang aims to fix this problem by using `feedback` data from our robot. Feedback data could be values from its [encoders](https://en.wikipedia.org/wiki/Encoder) (how far it has gone), [gyro](https://en.wikipedia.org/wiki/Gyroscope) (where it's pointing), or really anything else that we want to control.

The important thing is that the data are `real-time` - the robot constantly gives feedback about what it's doing and the controller acts accordingly.

Bang-bang is pretty much an implementation of the very first idea that comes to mind when we realize we can use the values from the position of the robot: simply say to drive, until we pass the goal!

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
        if self.get_feedback_value() < self.goal:
            return 1
        else:
            return 0
```

Regarding accuracy: this is already markedly better than our previous dead reckoning approach, but it is still relatively inaccurate, thanks to robot's inertia when the controller tells it that it shouldn't be driving anymore.

We could try to fix this by saying that once it passes the goal, it should start driving back, but the only thing you'd get is a robot that drives back and forward across the goal (which may be amusing, but not very helpful).

In the next chapters, we will try to improve our approach using feedback and create controllers that don't just return 1 for driving and 0 for standing still, but also values in-between (when the robot should be driving slower).
