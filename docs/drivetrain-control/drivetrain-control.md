---
layout: default
title: Drivetrain Control
nav_order: 10
has_children: true
permalink: drivetrain-control/
---

# Drivetrain Control
{:.no_toc}

Algorithms and techniques used to control the motors of the robot's **[drivetrains](https://en.wikipedia.org/wiki/Drivetrain)**.
{: .fs-6 .fw-300 }

![Drivetrain]({{site.url}}/assets/images/drivetrain-control/drivetrain.png "Drivetrain")

[Drivetrain image source](https://pictures.topspeed.com/IMG/crop/201604/2017-audi-tt-rs-44_1600x0w.jpg)
{: .fs-1 style="text-align: right;" }

---

The drivetrain of a vehicle is a group of components that deliver power to the driving wheels, hold them together and allow them to move. Some of the [most popular ones](http://www.simbotics.org/resources/mobility/drivetrain-selection) are:
- **tank drive** -- left and right side motors are driven independently -- like a *tank*
- **mecanum drive** -- similar to tank drive, but uses [mecanum wheels](http://www.wcproducts.net/wheels-hubs/mecanum-wheels), each of which is driven independently -- allows for more maneuverability
- **swerve drive** -- each wheel can rotate vertically around its axis -- the robot can drive and rotate in any direction

For the purpose of this guide, however, we will only be discussing some of the most frequently used drivetrains, and the methods to operate them.

Modified {% last_modified_at %B %-d, %Y %}
{: .fs-2 style="text-align: right;" }