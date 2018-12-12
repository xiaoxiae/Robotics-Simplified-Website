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
- `set_goal` is called to set the controller's goal. Goal can be any number. Note that we need to call this function before we try to get a value from the controller, or things will start to break.
- `get_value` will return the value that the controller thinks we should set the motors to to achieve our goal. **All controllers will return a value from -1 to 1.**

For this to make more sense, let's look at some concrete examples of popular motor controllers.
