<div id="sketch-holder" class="text-center"></div>
<script src="../../assets/js/p5.min.js"></script>
  <script>
  function setup() {
  	textStyle(NORMAL);
  }

  function setup() {
    var width = document.getElementById('sketch-holder').offsetWidth;
  	const canvas = createCanvas(width / 1.5, width / 1.5);
    canvas.parent('sketch-holder');
  	textStyle(NORMAL);
  	colorMode(HSB)
  }

  function draw() {
  	background(255);

  	dot_size = 30 / 800 * width

  	translate(width / 2, height / 2)
	  scale(0.99)

  	strokeWeight(3)
  	fill(255)
  	ellipse(0, 0, width, height)

  	strokeWeight(1)
  	line(-width / 2, 0, width / 2, 0)
  	line(0, -height / 2, 0, height / 2)

  	x = (mouseX - width / 2) / float(width / 2)
  	y = (mouseY - height / 2) / float(height / 2)

  	if (x > 1) x = 1
  	if (x < -1) x = -1
  	if (y > 1) y = 1
  	if (y < -1) y = -1

  	edge_distance = sqrt(pow(x / float(max(abs(x), abs(y))), 2) + pow(y / float(max(abs(x), abs(y))), 2))

  	fill(120, 100, 100)
  	ellipse(x / edge_distance * width / 2, y / edge_distance * width / 2, dot_size, dot_size)

  	fill(260, 260, 260)
  	ellipse(x * sqrt(1 - y * y / 2) * width / 2, y * sqrt(1 - x * x / 2) * width / 2, dot_size, dot_size)

  	if (sqrt(x * x + y * y) > 1) {
  		temp = sqrt(x * x + y * y)
  		x = x / temp
  		y = y / temp

  		fill(0, 150, 150)
  		ellipse(x * width / 2, y * width / 2, dot_size, dot_size)
  	}

  	fill(0)
  	ellipse(mouseX - width / 2, mouseY - height / 2, dot_size, dot_size)
  }

  function windowResized() {
    var width = document.getElementById('sketch-holder').offsetWidth;
    resizeCanvas(width / 1.5, width / 1.5);
  }
  </script>
