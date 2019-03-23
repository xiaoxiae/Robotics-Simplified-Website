# initialize objects that control robot components
left_motor = Motor(1)
right_motor = Motor(2)
gyro = Gyro()

# create a controller object and set its goal
controller = PID(0.2, 0.002, 0.015, time, gyro)
controller.set_goal(0)  # the goal is 0 because we want to head straight

while True:
    # get the controller value
    controller_value = controller.get_value()

    # drive the robot using arcade drive controlled by the controller value
    arcade_drive(controller_value, 0, left_motor, right_motor)
