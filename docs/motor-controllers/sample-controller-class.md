---
layout: default
title: Sample Controller Class
nav_order: 1
parent: Motor Controllers
permalink: motor-controllers/sample-controller-class/
---

# Sample Controller Class
Let's look at how classes of each of the controllers described in the sections above will look like:

```python
class SampleControllerClass:
    """Description of the class."""

    def __init__(self, ...):
        """Creates a controller object."""
        pass


    def set_goal(self, goal):
        """Sets the goal of the controller."""
        pass


    def get_value(self):
        """Returns the current controller value"""
        pass
```

Let's break it down function by function:
- `__init__` is called when we want to create the controller object. In the actual controller implementations, `...` will be replaced by the parameters that the controller takes.
- `set_goal` is called to set the controller's goal, where goal has to be a number. Note that we will need to call this function before we try to get a value from the controller, or things will start to break. This makes logical sense, because the controller can't really help you to reach a goal if you haven't specified the goal.
- `get_value` will return the value that the controller thinks we should set the motors to to achieve our goal. **All controllers will return a value between -1 and 1** (including 1 and -1).

All of this will make more sense as we go through each of the controllers.
