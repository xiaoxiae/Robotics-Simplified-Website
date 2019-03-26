# initialize objects that control robot components
left_motor = Motor(1)
right_motor = Motor(2)
joystick = Joystick()

# repeatedly set motors to the values of the axes
while True:
    # get axis values
    x = joystick.get_y1()
    y = joystick.get_y2()

    # drive the robot using adcade drive
    arcade_drive(x, y, left_motor, right_motor)