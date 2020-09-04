# initialize objects that control robot components
left_motor = Motor(1)
right_motor = Motor(2)

# create a controller object and set its goal
controller = DeadReckoning(2.5, get_current_time)
controller.set_goal(10)

while True:
    # get the controller value
    controller_value = controller.get_value()

    # drive the robot using tank drive controlled by the controller value
    tank_drive(controller_value, controller_value, left_motor, right_motor)