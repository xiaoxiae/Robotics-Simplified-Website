---
layout: default
title: Dead Reckoning
nav_order: 2
parent: Motor Controllers
permalink: motor-controllers/dead-reckoning/
---

# Dead reckoning ([wiki](https://en.wikipedia.org/wiki/Dead_reckoning))

## Introduction
One of the simplest ways of controlling the robot autonomously is using dead reckoning.

It is essentially what you would do on one of the first physics classes: measure the average speed over a certain distance. Once you have that, you can then calculate how long it would take to drive some other distance.

Say your robot drives an average of `v = 2.5m/s`. You have a `d = 10m` that you want the robot to drive. To calculate, how long it should take the robot, all you have to do is divide distance by speed: `t = d / v = 10 / 2.5 = 4s`.

---

## Implementation
There are two things that the controller needs: the **average speed** of the robot and a way to measure how much time had passed. Taking this into consideration, this is how a dead reckoning controller implementation could look like:

```python
class DeadReckoning:
    """A class implementing a dead reckoning controller."""

    def __init__(self, speed, get_current_time):
        """Initialises a Dead reckoning controller object from a function that
        returns current time and the average speed of the robot."""
        self.get_current_time = get_current_time
        self.speed = speed


    def set_goal(self, goal):
        """Sets the goal of the controller (also starts the controller)."""
        self.goal = goal
        self.start_time = self.get_current_time()


    def get_value(self):
        """Return the current value the controller is returning."""
        # at what time should we reach the destination (t=t_0 + s/v)
        arrival_time = self.start_time + self.goal / self.speed

        # return +-1 if we should have reached the destination and 0 if not
        if self.get_current_time() < arrival_time:
            return 1 if self.goal > 0 else -1
        else:
            return 0
```

**ADD AN EXAMPLE***

Although this is quite a simple controller to implement, you might realize that it is not too accurate. If the robot hits a bump on the road or changes heading, there is nothing it can do to correct itself, since it doesn't know where it's going.
