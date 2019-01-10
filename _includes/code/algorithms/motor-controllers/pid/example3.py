# create robot's motors, gyro and the encoder
left_motor = Motor(1)
right_motor = Motor(2)
gyro = Gyro()
encoder = Encoder()

# create separate controllers for turning and driving
drive_controller = PID(0.07, 0.001, 0.002, time, encoder)
turn_controller = PID(0.2, 0.002, 0.015, time, gyro)

# we want to stay at 0 degrees and drive 10 meters at the same time
turn_controller.set_goal(0)
drive_controller.set_goal(10)

while True:
    # get the values from both controllers
    turn_value = turn_controller.get_value()
    drive_value = drive_controller.get_value()

    # drive/turn using arcade drive
    arcade_drive(turn_value, drive_value, left_motor, right_motor)