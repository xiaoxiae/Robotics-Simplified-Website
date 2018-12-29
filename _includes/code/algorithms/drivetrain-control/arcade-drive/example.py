# create robot's motors and the joystick
left_motor = Motor(1)
right_motor = Motor(2)
joystick = Joystick()

# continuously set motors to the values on the axes
while True:
    # get axis values
    x = joystick.get_y1()
    y = joystick.get_y2()

    # drive the robot using tank drive
    arcade_drive(x, y, left_motor, right_motor)
