---
layout: default
title: Arcade Drive
nav_order: 2
parent: Drivetrain Control
permalink: drivetrain-control/arcade-drive/
---

# Arcade drive
Arcade drive is a method of controlling the motors of a robot using two axes of a controller, where one of the axes operates the "turning" component of the robot, and one the "driving" component of the robot (as if you were playing a game at an *arcade*).

![Arcade Drive]({{site.url}}/assets/images/drivetrain-control/arcade-drive.png "Arcade Drive")


## Implementation
Suppose that we have a joystick with an $$x$$ (horizontal) and a $$y$$ (vertical) axis.

There are many ways to get to the resulting arcade drive equations (for example by using [linear interpolation](https://www.chiefdelphi.com/media/papers/download/3495) for all of the 4 quadrants of the joystick input).

Here is the implementation we get by splitting the values into quadrants:

```python
def arcade_drive(rotate, drive, left_motor, right_motor):
    # variables to determine the quadrants
    maximum = max(abs(drive), abs(rotate))
    total, difference = drive + rotate, drive - rotate

    # set speed according to the quadrant that we're in.
    if drive >= 0:
        if rotate >= 0: # I quadrant
            left_motor(maximum)
            right_motor(difference)
        else:           # II quadrant
            left_motor(total)
            right_motor(maximum)
    else:
        if rotate >= 0: # IV quadrant
            left_motor(total)
            right_motor(-maximum)
        else:           # III quadrant
            left_motor(-maximum)
            right_motor(difference)
```


## Examples
Here's a program that makes the robot drive using the values from the joystick:

```python
# create robot's motors and the joystick
left_motor = Motor(1)
right_motor = Motor(2)
joystick = Joystick()

# continuously set motors to the values on the axes
while True:
    # get axis values
    x = joystick.get_y1()
    y = joystick.get_y2()

    # drive the robot using tank drive
    arcade_drive(x, y, left_motor, right_motor)
```


## Visualization
Here is a quick interactive visualization of the sorts of values our function sets the motors to for different values of $$x$$ and $$y$$:

<div id="sketch-holder"></div>
<script src="../../assets/js/p5.min.js"></script>
  <script>
  function setup() {
    var width = document.getElementById('sketch-holder').offsetWidth;
  	const canvas = createCanvas(width, width);
    canvas.parent('sketch-holder');
  	textStyle(NORMAL);
  }

  function draw() {
  	background(255);

    textSize(26)
    fill(200)
    textAlign(CENTER, TOP)
    text("Arcade drive visualisation", width / 2, 20)
	  textAlign(CENTER, CENTER)
    text("II", width/4, height/4)
    text("I", width * 3/4, height/4)
    text("III", width/4, height * 3/4)
    text("IV", width * 3/4, height * 3/4)
    textSize(13)

  	scale(1, -1);
  	translate(width / 2, -height / 2);

  	y = float(-mouseY + height / 2) / (height / 2)
  	x = float(mouseX - width / 2) / (width / 2)

    if (x > 1) x = 1
    if (x < -1) x = -1
    if (y > 1) y = 1
    if (y < -1) y = -1

    fill(0)
    ellipseMode(CENTER)
    ellipse(x * width / 2, y * height / 2, 2, 2)
    textAlign(CENTER, CENTER)
    drawText("(" + Number(x.toFixed(2)) + ", " + Number(y.toFixed(2)) + ")", x * width / 2, y * height / 2 + 12)

    stroke(230)
    strokeWeight(1)
    line(-width/2, y * height / 2, width/2, y * height / 2)
    line(x * width / 2, -height/2, x * width / 2, height/2)
    stroke(0)

  	stroke(130)
  	strokeWeight(1)
  	line(-width / 2, 0, width / 2, 0)
  	line(0, -height / 2, 0, height / 2)
  	stroke(0)

  	strokeWeight(2.2)
  	line(0, 0, x * width / 2, 0)
  	line(0, 0, 0, y * height / 2)
  	strokeWeight(0)

  	fill(0)
  	textAlign(LEFT, CENTER)
  	drawText("y", 5, y * height / 4)

  	textAlign(CENTER, BOTTOM)
  	drawText("x", x * width / 4, 5)

  	motorSpeeds = arcadeDrive(x, y)

  	stroke(0)
  	strokeWeight(1)
  	line(width / 4, 0, width / 4, motorSpeeds[1] * height / 2)
  	line(-width / 4, 0, -width / 4, motorSpeeds[0] * height / 2)
  	strokeWeight(0)

    fill(0)
    textAlign(CENTER, CENTER)
    drawText("Right Motor\n" + Number(motorSpeeds[1].toFixed(2)), width / 4, motorSpeeds[1] * height / 4)
    drawText("Left Motor\n" + Number(motorSpeeds[0].toFixed(2)), -width / 4, motorSpeeds[0] * height / 4)
  }

  function arcadeDrive(x, y) {
  	maximum = max(abs(y), abs(x))
  	total = y + x
  	difference = y - x

  	if (y >= 0) {
  		if (x >= 0) return [maximum, difference]
  		else return [total, maximum]
  	} else {
  		if (x >= 0) return [total, -maximum]
  		else return [-maximum, difference]
  	}
  }

  function drawText(string, x, y, rotateBy = 0) {
  	push()
  	translate(x, y)
  	scale(1, -1)
  	rotate(rotateBy)
  	text(string, 0, 0)
  	pop()
  }

  function windowResized() {
    var width = document.getElementById('sketch-holder').offsetWidth;
    resizeCanvas(width, width);
  }
  </script>


## Closing remarks
If you are interested in reading more about this topic, I would suggest looking at [this thread on Chief Delphi](https://www.chiefdelphi.com/media/papers/2661), where I learned most of the information about the theory behind arcade drive.
