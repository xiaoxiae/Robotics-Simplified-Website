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

It is essentially what most people do in their very first physics class: measure the average speed of something. We can then calculate, how much time would it take for the something (in our case the robot) to drive that distance.

Let's look at an example: say your robot drives an average of `v = 2.5m/s`. You have a distance of `d = 10m` that you want the robot to drive. To calculate, how long it should take the robot, all you have to do is divide distance by speed: `t = d/v = 10/2.5 = 4s`.

---

## Implementation
There are two things that the controller needs: the average speed of the robot and a way to measure how much time had passed. Taking this into consideration, this is how a dead reckoning controller implementation could look like:

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
        # at what time should we reach the destination (d=d_0 + s/v)
        arrival_time = self.start_time + (self.goal / self.speed)

        # if current time is less than the arrival time, we should be driving
        if self.get_current_time() < arrival_time:
            return 1
        else:
            return 0
```

Let's implement the example mentioned above to make the robot drive 10 meters:

```python
# create robot's motors and the joystick
l_motor = Motor(1)
r_motor = Motor(2)
joystick = Joystick()

# create the controller object
# time is a function that returns current time when called
controller = DeadReckoning(2.5, time)

# set the goal for the controller (10 meters)
controller.set_goal(10)

# while the controller is telling us to drive forward, run both motors
while controller.get_value():
    l_motor(1)
    r_motor(1)
```

Although this is quite a simple controller to implement, you might realize that it is not too accurate. If the robot hits a bump on the road or slips on a banana peel, there is nothing it can do to correct the error (since it doesn't know where it's going).

We'll be focusing on improving accuracy in the next few upcoming chapters by incorporating real-time data from the robot in our controllers.
