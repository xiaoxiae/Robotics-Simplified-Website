# initialize objects that control robot components
left_motor = Motor(1)
right_motor = Motor(2)
encoder = Encoder()

# create a controller object and set its goal
controller = PolynomialFunction([-15.69, 30.56, -21.97, 6.91, 0.2], encoder)
controller.set_goal(10)

while True:
    # get the controller value
    controller_value = controller.get_value()

    # drive the robot using tank drive controlled by the controller value
    tank_drive(controller_value, controller_value, left_motor, right_motor)
