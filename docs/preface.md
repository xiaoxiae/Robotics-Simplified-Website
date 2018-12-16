---
layout: default
title: Preface
nav_order: 2
permalink: preface/
---

# Preface
{:.no_toc}

Although you don't need to know any robotics before reading through this website, there are some things that can make your learning experience much more pleasant.

---

## Programming Language
Understand basic concepts of programming will definitely come in handy before reading through the project. There are lots of great resources for learning programming:
- [Reddit r/learnprogramming](https://www.reddit.com/r/learnprogramming/)
- [Codeacademy](https://www.codecademy.com/) and their [Learn Python 3](https://www.codecademy.com/learn/learn-python-3) course
- [Project Euler](https://projecteuler.net/) for practicing programming on fun math-based problems.

Familiarity with Python's syntax would also be good, since all of the code examples discussed in the project are in Python. If you don't know much about Python but already know how to program in a different language, [Dive into Python 3](http://histo.ucsf.edu/BMS270/diveintopython3-r802.pdf) is a great place to start.

It is also recommended to know a little about [object-oriented programming](https://en.wikipedia.org/wiki/Object-oriented_programming), since we will be basing most of the programs on objects of various classes.

If you don't know programming at all (and don't have the time to learn) but are interested in learning about robotics, you can still read through the chapters - the code is there mainly as examples for those who are interested in the possible ways to implement the concepts.


## Libraries and Classes
Throughout the project, there will be a lot of made-up classes like `Motor`, `Joystick` and `Gyro`. They are only used as placeholders for real classes that you would (likely) have if you were implementing some of the concepts covered on this website.


## Running the code
All of the code on this website has been tested on a [VEX EDR](https://www.vexrobotics.com/vexedr) robot programmed in Python using [RobotMesh](https://www.robotmesh.com/). If you want to try out the code, doing the same would be easiest - all you'd have to do is substitute the made-up classes and methods for real ones from the vex library and run the code.

An alternative is to use methods from [`utilities.py`](https://github.com/xiaoxiae/Robotics-Simplified/blob/master/Code/algorithms/utilities.py) to test out the values the objects/methods return.
