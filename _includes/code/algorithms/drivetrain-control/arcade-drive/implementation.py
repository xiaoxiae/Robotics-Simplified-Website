def arcade_drive(rotate, drive, left_motor, right_motor):
    """Drives the robot using arcade drive."""
    # variables to determine the quadrants
    maximum = max(abs(drive), abs(rotate))
    total, difference = drive + rotate, drive - rotate

    # set speed according to the quadrant that the values are in
    if drive >= 0:
        if rotate >= 0:  # I quadrant
            left_motor(maximum)
            right_motor(difference)
        else:            # II quadrant
            left_motor(total)
            right_motor(maximum)
    else:
        if rotate >= 0:  # IV quadrant
            left_motor(total)
            right_motor(-maximum)
        else:            # III quadrant
            left_motor(-maximum)
            right_motor(difference)