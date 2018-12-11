---
layout: default
title: Sample Motor Controller Class
nav_order: 1
parent: Motor Controllers
permalink: motor-controllers/sample-motor-controller-class/
---

# Sample controller class
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

Let's break it down piece by piece:
- `__init__` is a method called when we want to create the controller object.
- `set_goal` will be called to set the goal that the controller should aim for.
- `get_value` will return the value that the controller thinks we should set the motors to.

This will make more sense once you see the actual classes of controllers, but it's a good resource to refer to when you need it.
