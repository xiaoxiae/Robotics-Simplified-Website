---
layout: default
title: Bang-bang
nav_order: 3
parent: Motor Controllers
permalink: motor-controllers/bang-bang/
---

# Bang–bang
Although our previous controller was quite easy to implement and use, there is no way for it to know whether it reached the target or not. It pretty much just turns the motors on for a while and hopes for the best.

[Bang-bang](https://en.wikipedia.org/wiki/Bang%E2%80%93bang_control) aims to fix this problem by using [feedback](https://en.wikipedia.org/wiki/Feedback) from our robot. Feedback could be values from its [encoders](https://en.wikipedia.org/wiki/Encoder) (to measure how far it has gone), [gyro](https://en.wikipedia.org/wiki/Gyroscope) (to measure where it's heading), or really anything else that we wish to control. The important thing here is that the data is **real-time**. The robot continuously tells the controller what is happening, so the controller can act accordingly.

Bang-bang implements the very first idea that comes to mind when we have real-time data available. The controller will return 1 if we haven't passed the goal yet and 0 if we have.


## Implementation
The only thing the Bang-bang controller needs is the feedback function returning information about the state of whatever we're trying to control.

```python
{% include code/algorithms/motor-controllers/bang-bang/implementation.py %}
```

## Examples
To make the robot drive a distance using this controller, we need a new `Encoder` class to measure how far the robot has driven. The objects of this class return the average of the distance driven by the left wheel and by the right wheel.

```python
{% include code/algorithms/motor-controllers/bang-bang/example.py %}
```

Notice that pretty much nothing changed between this and the dead reckoning example. This is the main advantage of all of the controllers having the same functions -- we can use controller objects almost interchangeably, allowing us to easily try out and compare the accuracies of each of the controllers, without messing with the rest of our code.


## Closing remarks
This is already markedly better than our previous dead reckoning approach, but it is still relatively inaccurate: the robot's inertia will make the robot drive a little extra distance when the controller tells it that it shouldn't be driving anymore, which means it will likely overshoot.

We could try to fix this by saying that it should start driving backward once it passed the goal, but the only thing you'd get is a robot that drives back and forth across the goal (which may be amusing, but not very helpful).

In the upcoming articles, we will try to improve our approach and create controllers that don't just return 1 for driving and 0 for not driving, but also values in-between (when the robot should be driving slower and when faster).

Modified {% last_modified_at %B %-d, %Y %}
{: .fs-2 style="text-align: right;" }