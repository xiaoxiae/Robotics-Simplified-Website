# create robot's motors, gyro and the encoder
left_motor = Motor(1)
right_motor = Motor(2)
encoder = Encoder()

# create the PID controller (with encoder being the feedback function)
controller = PID(0.07, 0.001, 0.002, time, encoder)
controller.set_goal(10)

while True:
    # get the speed from the controller and apply it using tank drive
    value = controller.get_value()
    tank_drive(value, value, left_motor, right_motor)