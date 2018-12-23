---
layout: default
title: Bang-bang
nav_order: 3
parent: Motor Controllers
permalink: motor-controllers/bang-bang/
---

# Bang–bang ([wiki](https://en.wikipedia.org/wiki/Bang%E2%80%93bang_control))
Although our previous controller was quite easy to implement and use, there is no way for it to know whether it reached the target or not. It pretty much just turns the motors on for a while and hopes for the best.

Bang-bang aims to fix this problem by using [`feedback`](https://en.wikipedia.org/wiki/Feedback) from our robot. Feedback could be values from its [encoders](https://en.wikipedia.org/wiki/Encoder) (to measure how far it has gone), [gyro](https://en.wikipedia.org/wiki/Gyroscope) (to measure where it's heading), or really anything else that we want to control. The important thing is that the data are **real-time** - the robot constantly gives feedback about what is happening to the controller, so the controller can act accordingly.

Bang-bang is the very first idea that comes to mind when we have real-time data. The controller will return 1 if we haven't passed the goal yet and 0 if we have.


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

## Examples
For this example, we need an `Encoder` class to measure how far the robot has driven. The objects of this class will return the average of the distance driven by the left wheel and by the right wheel. Her is how a program that drives the robot 10 meters will look like:

```python
# create robot's motors and the encoder
left_motor = Motor(1)
right_motor = Motor(2)
encoder = Encoder()

# create the controller object and set its goal
controller = Bangbang(encoder)
controller.set_goal(10)

# while the controller is telling us to drive forward, drive forward
while controller.get_value() == 1:
    tank_drive(1, 1, left_motor, right_motor)
```

Notice that pretty much nothing changed between this and the dead reckoning example. This is the main advantage of all of the controllers having the same functions - we can use controller objects almost interchangeably, allowing us to easily try out and compare the accuracies of each of the controllers, without messing with the rest of our code.


## Closing remarks
This is already markedly better than our previous dead reckoning approach, but it is still relatively inaccurate: the robot's inertia will make the robot drive a little extra distance when the controller tells it that it shouldn't be driving anymore, which means it will overshoot.

We could try to fix this by saying that it should start driving backward once it passed the goal, but the only thing you'd get is a robot that drives back and forth across the goal (which may be amusing, but not very helpful).

In the next chapters, we will try to improve our approach and create controllers that don't just return 1 for driving and 0 for not driving, but also values in-between (when the robot should be driving slower and when faster).
