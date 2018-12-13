---
layout: default
title: Preface
nav_order: 2
permalink: preface/
---

# Preface
{:.no_toc}

Although the website is very accessible to anyone who doesn't know anything about robotics, there are some things that can make the learning experience much more pleasant. 

---

## Programming Language
Before going through the website, it is recommended that you understand basic concepts of programming (preferably in Python, since all of the implementations discussed in the project are in Python) before reading through the project. If you don't know much about Python but would like to learn, [Dive into Python 3](http://histo.ucsf.edu/BMS270/diveintopython3-r802.pdf) is a great place to start.

It is also recommended to know a little about [object-oriented programming](https://en.wikipedia.org/wiki/Object-oriented_programming), since we will be basing most of the programs on objects of various classes.

If you don't know programming at all but are interested in learning about robotics, you can still read through the chapters, the code is there mainly to help you understand how the concepts could be implemented.

## Libraries and Classes
Throughout the project, there will be a lot of made-up classes like `Motor`, `Joystick` and `Gyro`. They are only used as placeholders for real classes that you would (likely) have if you were implementing some of the concepts covered on this website.

## Running the code
The code on the website has been tested on a [VEX EDR](https://www.vexrobotics.com/vexedr) robot programmed in Python using [RobotMesh](https://www.robotmesh.com/). If you want to try out the code, doing the same would be easiest - all you'd have to do is substitute the made-up classes and methods for real ones from the vex library and (pretty much) run the code as is.

An alternative is to use methods from [`utilities.py`](https://github.com/xiaoxiae/Robotics-Simplified/blob/master/Code/algorithms/utilities.py) to test out the values the controllers/methods return.
