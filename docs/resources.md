---
layout: default
title: Resources
nav_order: 40
permalink: resources/
---

# Resources
{:.no_toc}

Links to resources either directly used by the website (such as libraries), or those that helped me understand the concepts mentioned in the articles.

---

## Math
The website uses [$$\text{\KaTeX}$$](https://katex.org/) to render $$\text{\LaTeX}$$ equations.

## Images
The images used to illustrate the concepts on this website are modified using [Inkscape](https://inkscape.org/cs/) (free vector graphics editor) and [GIMP](https://www.gimp.org/) (free bitmap graphics editor). CAD model images are generated with [Fusion 360](https://www.autodesk.com/products/fusion-360/students-teachers-educators) (free CAD design software, assuming you are a student). I also used the [TinyPNG](https://tinypng.com/) website to compress the images.

## p5.js
Visualizations on the website are created using the [p5.js](https://p5js.org/) library. This [example](https://raw.githubusercontent.com/KevinWorkman/HappyCoding/gh-pages/examples/p5js/_posts/2018-07-04-fireworks.md) helped me understand how it worked with Jekyll. I use the [p5js web editor](https://editor.p5js.org/) to edit the visualizations before I put them on the website.

## VEX EDR
To test the algorithms, I built a custom VEX EDR robot using [this kit](https://www.vexrobotics.com/276-3000.html) that the educational center [VCT](http://www.vctu.cz/) kindly lent me. The robot is programed in Python using [RobotMesh studio](https://www.robotmesh.com/studio) (for more information, see the Python [documentation](https://www.robotmesh.com/docs/vexcortex-python/html/namespaces.html)).

## Autonomous motion control
[PythonRobotics](https://github.com/AtsushiSakai/PythonRobotics) is a great repository containing implementations of various robotics algorithms in Python.

## PID
I studied a PID Python [implementation](https://github.com/ivmech/ivPID) before writing my own.

## Drivetrain Control
There were a few helpful articles that helped me understand equations behind the more complex drivetrains:
- Arcade drive Chief Delphi forum [post](https://www.chiefdelphi.com/media/papers/2661) by Ether.
- Simplistic Control of Mecanum Drive [paper](https://forums.parallax.com/discussion/download/79828/ControllingMecanumDrive%255B1%255D.pdf&sa=U&ved=0ahUKEwiX5LzFiNrfAhVswYsKHTofDrwQFggEMAA&client=internal-uds-cse&cx=002870150170079142498:hq1zjyfbawy&usg=AOvVaw19D74YD--M3YmQ2MGd1rTg).
- Swerve drive Chief Delphi forum [post](https://www.chiefdelphi.com/t/paper-4-wheel-independent-drive-independent-steering-swerve/107383) by Ether.

## Circle Approximation
There were two main resources that helped me write the Circle Approximation article.
- Kinematics Equations for Differential Drive and Articulated Steering [whitepaper](http://www8.cs.umu.se/kurser/5DV122/HT13/material/Hellstrom-ForwardKinematics.pdf)
- Position Estimation [presentation](http://people.scs.carleton.ca/~lanthier/teaching/COMP4807/Notes/5%20-%20PositionEstimation.pdf)

Modified {% last_modified_at %B %-d, %Y %}
{: .fs-2 style="text-align: right;" }
