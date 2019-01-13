---
layout: default
title: Motor Controllers
nav_order: 4
has_children: true
permalink: motor-controllers/
---

# Motor controllers
{:.no_toc}

Autonomous control of the robot using [motor controllers](https://en.wikipedia.org/wiki/Motor_controller).
{: .fs-6 .fw-300 }

---

It's nice to be able to drive the robot around using a joystick, but it would sometimes be more useful if the robot could drive **autonomously** (something functioning independently). This is where controllers come in.

A controller is a box that takes in information about the robot and a goal that we want the robot to achieve (like drive a certain distance / turn a certain angle) and, when asked, spits out values it thinks the robot should set its motors to, to achieve that goal.

The are lots of various controllers to choose from that differ in many ways, such as:
- **Accuracy** - how accurate is the controller in getting the robot where it needs to be? How error-prone is it to unexpected situations (a bump on the road, motor malfunction,...).
- **Input** - what of information does the controller needs to function properly (and accurately)? Does the information have to be real-time?
- **Complexity** - how difficult is it to implement/configure said controller? How computationally intensive it is?

There is a whole field of study called [control theory](https://en.wikipedia.org/wiki/Control_theory) that examines controllers much more comprehensively than we can in a few short articles. That's why we're only going to talk about a select few.

Modified {% last_modified_at %B %-d, %Y %}
{: .fs-2 style="text-align: right;" }