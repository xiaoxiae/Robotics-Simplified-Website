---
layout: default
title: PID
nav_order: 4
parent: Motor Controllers
permalink: motor-controllers/pid/
---

# PID ([wiki](https://en.wikipedia.org/wiki/PID_controller))
Our previous attempt at creating a controller that used feedback from the robot could be further improved by considering how the **error** (difference between feedback value and the goal) changes over time.

Since PID is an abbreviation, let's talk about that the terms $$P$$, $$I$$ and $$D$$ mean:
- $$P$$ stands for **proportional** - how large is the error now (in the **present**).
- $$I$$ stands for **integral** - how large the error (accumulatively) was in the **past.**
- $$D$$ stands for **derivative** - what will the error likely be in the **future.**

The controller takes into account what happened, what is happening, and what will likely happen and continuously calculates each of the terms as the error changes:

![PID]({{site.url}}/assets/images/motor-controllers/pid.png "PID")

[PID image source](https://upload.wikimedia.org/wikipedia/commons/4/40/Pid-feedback-nct-int-correct.png)
{: .fs-1 style="text-align: right;" }


## Implementation
The controller will need $$p$$, $$i$$ and $$d$$ constants to know, how important each of the aforementioned parts (proportional, integral, derivative) are. It will also need a feedback function and, to correctly calculate the integral and derivative, a function that returns the current time:

```python
{% include code/algorithms/motor-controllers/pid/implementation.py %}
```

To fully understand how the controller works, I suggest you closely examine the `get_value()` function - that's where all the computation happens.

Notice a new function called `reset`, that we haven't seen in any of the other controllers. It is called every time we set the goal, because the controller accumulates error over time in the `self.integral` variable, and it would therefore take longer to adjust to the new goal.

It doesn't change the versatility of the controller classes, because we don't need to call it in order for the controller to function properly, it's just a useful function to have if we want to call it manually.


## Tuning the controller
PID is the first discussed controller that needs to be tuned correctly to perform well, because if you set the constants to the wrong values, the controller will perform [poorly](https://www.youtube.com/watch?v=MxALJU_hp34).

There is a [whole section](https://en.wikipedia.org/wiki/PID_controller#Loop_tuning) on Wikipedia about PID tuning. We won't go into details (read through the Wikipedia article if you're interested), but it is just something to keep in mind when using PID.


## Examples

### Driving a distance
Here is an example that makes the robot drive 10 meters forward. The constants are values that I used on the VEX EDR robot that I built to test the PID code, you will likely have to use different ones:

```python
{% include code/algorithms/motor-controllers/pid/example1.py %}
```


### Auto-correct heading
Auto-correcting the heading of a robot is something PID is great for. What we want is to program the robot so that if something (like an evil human) pushes it, the robot adjusts itself to head the way it was heading before the push.

We could either use values from the encoders on the left and the right side to calculate the angle, but a more elegant (and accurate) solution is to use a gyro. Let's therefore assume that we have a `Gyro` class whose objects give us the current heading of the robot.

One thing we have to think about is what to set the motors to when we get the value from the controller, because to turn the robot, both of the motors will be going in opposite directions. Luckily, `arcade_drive` is our savior: we can plug our PID values directly into the turning part of arcade drive (the `x` axis) to steer the robot. Refer back to the [Arcade Drive article]({{site.baseurl}}drivetrain-control/arcade-drive/), if you are unsure as to how/why this works.

```python
{% include code/algorithms/motor-controllers/pid/example2.py %}
```


### Two controller combination
What's even nicer is that we can combine the two examples that we just implemented into ONE - a robot that drives forward and corrects itself when it isn't heading the right way.

We will create two controllers - one for driving straight by a certain distance and one for turning to correct possible heading errors.

Arcade drive will again be our dear friend, since we can plug values from the controller that controls driving directly into the driving part of arcade drive, and the controller that controls heading directly into the turning part of arcade drive:

```python
{% include code/algorithms/motor-controllers/pid/example3.py %}
```


## Closing remarks
PID is one of the most widely used controllers not just in robotics, but in many industries (controlling a boiler/thermostat) because it is reliable, relatively easy to implement and quite precise for most use cases.

For motivation, here is a [great video](https://www.youtube.com/watch?v=4Y7zG48uHRo) demonstrating the power of a correctly configured PID controller.