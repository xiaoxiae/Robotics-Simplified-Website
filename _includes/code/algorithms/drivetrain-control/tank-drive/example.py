# initialize objects that control robot components
left_motor = Motor(1)
right_motor = Motor(2)
joystick = Joystick()

# repeatedly set motors to the values of the axes
while True:
    # get axis values
    y1 = joystick.get_y1()
    y2 = joystick.get_y2()

    # drive the robot using tank drive
    tank_drive(y1, y2, left_motor, right_motor)
