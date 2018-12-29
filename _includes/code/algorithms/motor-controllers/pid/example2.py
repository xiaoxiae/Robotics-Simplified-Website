# create robot's motors and the gyro
left_motor = Motor(1)
right_motor = Motor(2)
gyro = Gyro()

# create the PID controller with gyro being the feedback function
controller = PID(0.2, 0.002, 0.015, time, gyro)
controller.set_goal(0)  # the goal is 0 - we want the heading to be 0

while True:
    # get the value from the controller
    value = controller.get_value()

    # set the turning component of arcade drive to the controller value
    arcade_drive(controller.get_value(), 0, left_motor, right_motor)