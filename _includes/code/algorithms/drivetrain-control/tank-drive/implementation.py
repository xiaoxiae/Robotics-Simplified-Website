def tank_drive(l_motor_speed, r_motor_speed, left_motor, right_motor):
    """Sets the speed of the left and the right motor."""
    left_motor(l_motor_speed)
    right_motor(r_motor_speed)