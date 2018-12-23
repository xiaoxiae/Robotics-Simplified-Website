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

It uses one of the first equations you learned in physics: `time = distance / average velocity`. We use it to calculate, how long it takes the robot to go a certain distance based on its average speed.

Let's look at an example: say our robot drives an average of `v = 2.5m/s`. We want it to drive a distance of `d = 10m`. To calculate, how long it will take the robot, all you have to do is divide distance by velocity: `t = d/v = 10/2.5 = 4s`.

This is exactly what dead reckoning does - it calculates the time it will take the robot to drive the distance to the goal. When asked, returns 1 if the time hasn't elapsed yet and 0 if it has.


## Implementation
There are two things that the controller needs: the average speed of the robot and a way to measure how much time had passed. Taking this into consideration, this is how a class implementing dead reckoning could look like:

```python
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

        # if current time is less than the arrival time, we should be driving
        if self.get_current_time() < arrival_time:
            return 1
        else:
            return 0
```

As we see, the parameters the `__init__` function is expecting to get are:
- `speed` - a number describing how fast the robot drives (on average) in units per second.
- `get_current_time` - a function returning the current time (used to measure, whether we should have arrived or not).


## Example
Let's implement the example mentioned in Introduction and make the robot drive 10 meters:

```python
# create robot's motors
left_motor = Motor(1)
right_motor = Motor(2)

# create the controller object and set its goal
controller = DeadReckoning(2.5, get_current_time)
controller.set_goal(10)

# while the controller is telling us to drive forward, drive forward
while controller.get_value() == 1:
    tank_drive(1, 1, left_motor, right_motor)
```

Notice how we used our previously implemented `tank_drive` function to set both motors to drive forward at a maximum speed. We could have just written `left_motor(1)` and `right_motor(1)`, but this is a cleaner way of writing it.


## Closing remarks
Although this is quite a simple controller to implement, you might realize that it is neither accurate nor practical. If the robot hits a bump on the road or slips on a banana peel, there is nothing it can do to correct the error (since it doesn't know where it is and where it's going).

Another important thing to keep in mind when using this controller is that if you want to change how fast the robot is driving/turning, you will need to re-calculate the speed of the robot to match said speed, which is very tedious.

We'll be focusing on improving accuracy in the next few upcoming chapters by incorporating real-time data from the robot in our controllers.
