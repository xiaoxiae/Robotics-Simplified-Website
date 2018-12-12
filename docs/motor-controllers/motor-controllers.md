---
layout: default
title: Motor Controllers
nav_order: 3
has_children: true
permalink: motor-controllers/
---

# Motor controllers
{:.no_toc}

Autonomous control of the robot using [motor controllers](https://en.wikipedia.org/wiki/Motor_controller).
{: .fs-6 .fw-300 }

---

## Introduction
It's nice to be able to drive around with the robot using a motor configuration of our choosing, but it would be much nicer to program it to drive autonomously (without external assistance). This is where controllers come in.

A controller is essentially a box that takes some information about the robot in and a goal that we want the robot to achieve (drive a certain distance / turn a certain angle...) and spits out values it thinks the robot should set its motors to, to achieve that goal.

The are a lot of controllers to choose from. They could differ in a lot of ways, such as:
- **Accuracy** - how accurate is the controller in getting the robot where it needs to be?
- **Input** - what of information does the controller needs to function properly (and accurately)?
- **Complexity** - how difficult is it to implement/configure the controller?

Although there is a whole field of study called [control theory](https://en.wikipedia.org/wiki/Control_theory) that examines the controllers in great lengths, we're going to talk about only a select few (namely the most frequently used ones in FRC).
