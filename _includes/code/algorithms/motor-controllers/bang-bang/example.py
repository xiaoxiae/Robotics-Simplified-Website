# create robot's motors and the encoder
left_motor = Motor(1)
right_motor = Motor(2)
encoder = Encoder()

# create the controller object and set its goal
controller = Bangbang(encoder)
controller.set_goal(10)

# while the controller is telling us to drive forward, drive forward
while controller.get_value() == 1:
    tank_drive(1, 1, left_motor, right_motor)
