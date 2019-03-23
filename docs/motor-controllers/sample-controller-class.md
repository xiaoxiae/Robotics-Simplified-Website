---
layout: default
title: Sample Controller Class
nav_order: 1
parent: Motor Controllers
permalink: motor-controllers/sample-controller-class/
---

# Sample Controller Class
Although each of the controllers will operate quite differently, they will all have (nearly) identical functions, that will allow us to use them interchangeably, without breaking the rest of the code.

```python
{% include code/algorithms/motor-controllers/sample-controller-class.py %}
```

`__init__` is called when we want to create a controller object. In the actual controller implementations, "`...`" will be replaced by the parameters that the controller takes.

`set_goal` is called to set the controller's goal, where goal has to be a number. Note that we will need to call this function before trying to call `get_value`, or things will break. This makes sense, because the controller can't really help you to reach the goal if you haven't specified it yet.

`get_value` will return the value that the controller thinks we should set the motors to, to achieve our goal. **All controllers will return values between (and including) -1 and 1,** since it's more convenient to do math on numbers in that range.

All of this will make more sense as we go through each of the controllers.

Modified {% last_modified_at %B %-d, %Y %}
{: .fs-2 style="text-align: right;" }