# create robot's motors and the joystick
left_motor = Motor(1)
right_motor = Motor(2)
joystick = Joystick()

# continuously set motors to the values on the axes
while True:
    # get axis values
    y1 = joystick.get_y1()
    y2 = joystick.get_y2()

    # drive the robot using tank drive
    tank_drive(y1, y2, left_motor, right_motor)
