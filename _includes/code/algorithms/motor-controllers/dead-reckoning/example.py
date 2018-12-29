# create robot's motors
left_motor = Motor(1)
right_motor = Motor(2)

# create the controller object and set its goal
controller = DeadReckoning(2.5, get_current_time)
controller.set_goal(10)

# while the controller is telling us to drive forward, drive forward
while controller.get_value() == 1:
    tank_drive(1, 1, left_motor, right_motor)