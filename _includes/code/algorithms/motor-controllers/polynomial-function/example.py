# create robot's motors, gyro and the encoder
left_motor = Motor(1)
right_motor = Motor(2)
encoder = Encoder()

# create the controller (with encoder as the feedback function)
controller = PolynomialFunction([-15.69, 30.56, -21.97, 6.91, 0.2], encoder)
controller.set_goal(10)

while True:
    # get the speed from the controller and apply it using tank drive
    value = controller.get_value()
    tank_drive(value, value, left_motor, right_motor)