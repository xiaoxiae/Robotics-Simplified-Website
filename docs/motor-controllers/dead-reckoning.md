---
layout: default
title: Dead Reckoning
nav_order: 2
parent: Motor Controllers
permalink: motor-controllers/dead-reckoning/
---

# Dead reckoning
One of the simplest ways of controlling the robot autonomously is using [dead reckoning](https://en.wikipedia.org/wiki/Dead_reckoning).

It uses one of the first equations you learned in physics: $$time = distance / velocity$$. We use it to calculate, how long it takes something to travel a certain distance based on its average speed.

Let's look at an example: say our robot drives an average of $$v = 2.5 \frac{m}{s}$$. We want it to drive a distance of $$d = 10m$$. To calculate, how long it will take the robot, all you have to do is divide distance by velocity: $$t = d/v = 10/2.5 = 4s$$.

This is exactly what dead reckoning does - it calculates the time it will take the robot to drive the distance to the goal. When asked, returns 1 if the time hasn't elapsed yet and 0 if it has.


## Implementation
There are two things that the controller needs: the average speed of the robot and a way to measure how much time had passed.

```python
{% include code/algorithms/motor-controllers/dead-reckoning/implementation.py %}
```

As we see, the parameters the `__init__` function is expecting to get are:
- `speed` - the average speed of the robot.
- `get_current_time` - a function returning the current time (used to measure, whether the calculated time had elapsed).


## Example
```python
{% include code/algorithms/motor-controllers/dead-reckoning/example.py %}
```

This is an implementation of the problem proposed in the Introduction: make a robot drive 10 meters.

Notice how we used our previously implemented `tank_drive` function to set both motors to drive forward. We could have written `left_motor(controller_value)` and `right_motor(controller_value)`, but this is a cleaner way of writing it.


## Closing remarks
Although this is quite a simple controller to implement, you might realize that it is neither accurate nor practical. If the robot hits a bump on the road or slips on a banana peel, there is nothing it can do to correct the error, since it doesn't know where it is.

Another important thing to keep in mind when using this controller is that if you want to change how fast the robot is driving/turning, you will need to re-calculate the average speed of the robot, which is tedious.

We'll be focusing on improving accuracy in the upcoming articles by incorporating real-time data from the robot into our controllers.

Modified {% last_modified_at %B %-d, %Y %}
{: .fs-2 style="text-align: right;" }