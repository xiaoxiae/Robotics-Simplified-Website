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

It is essentially what most people do in their very first physics class: calculate, how long it takes something to go a certain distance when we know its average speed.

Let's look at an example: say our robot drives an average of `v = 2.5m/s`. We want it to drive a distance of `d = 10m`. To calculate, how long it will take the robot, all you have to do is divide distance by velocity: `t = d/v = 10/2.5 = 4s`.

This is exactly what dead reckoning does - it calculates the time it will take for the robot to drive the specified distance and then returns 1 if the time hasn't elapsed yet (and 0 if it has).

_An important thing to keep in mind when using this controller is that if you want to change how fast the robot is driving/turning, you will need to re-calculate the speed of the robot to drive the correct distance._

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

Let's examine the parameters of the `__init__` function:
- `speed` is how fast the robot drives (on average, at a certain speed) in units per second.
- `get_current_time` is a function that when called returns the current time. To make things easier, we can assume that there is such function somewhere in our code.

## Example
Let's implement the example mentioned above to make the robot drive 10 meters:

```python
# create robot's motors
left_motor = Motor(1)
left_motor = Motor(2)

# create the controller object
controller = DeadReckoning(2.5, get_current_time)

# set the goal of the controller
controller.set_goal(10)

# while the controller is telling us to drive forward, drive forward
while controller.get_value() == 1:
    tank_drive(1, 1, left_motor, right_motor)
```

Notice how we used our previously implemented `tank_drive` function to set both motors to drive forward at a maximum speed. We could have just written `left_motor(1)` and `right_motor(1)`, but this is a cleaner way to write it.

## Closing remarks
Although this is quite a simple controller to implement, you might realize that it is not accurate nor practical. If the robot hits a bump on the road or slips on a banana peel, there is nothing it can do to correct the error (since it doesn't know where it's going). Alternatively, if you want the robot to drive the distance slower, you will need to re-calculate its average speed.

We'll be focusing on improving accuracy in the next few upcoming chapters by incorporating real-time data from the robot in our controllers.
