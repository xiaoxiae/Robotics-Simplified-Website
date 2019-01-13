def tank_drive(l_motor_speed, r_motor_speed, left_motor, right_motor):
    """Drives the robot using tank drive."""
    left_motor(l_motor_speed)
    right_motor(r_motor_speed)