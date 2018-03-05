#!/usr/bin/env python3
import ev3dev.ev3 as ev3

"""
Love is based on Braitenberg's vehicle 3A.
It will 'stay close by in quiet admiration from the time
it spots the source to all future time.' (Braitenberg, 1987)
"""

_amplify = 10
_threshold = 20
_maxIntensity = 50

motorLeft = ev3.LargeMotor('outA')
motorRight = ev3.LargeMotor('outD')

cSensorLeft = ev3.ColorSensor('in1')
cSensorRight = ev3.ColorSensor('in4')

btn = ev3.Button()

cSensorLeft.mode = 'COL-AMBIENT'
cSensorRight.mode = 'COL-AMBIENT'

def cleanup() -> None:
    """
    Stop all motors.

    Returns:
        None: Stops Ev3's Motors
    """
    motorLeft.stop()
    motorRight.stop()
    exit()

def btnstop(a_b) -> None:
    #TODO: Complete Docstring
    """

    Args:
        a_b ():

    Returns:
        None:
    """

    cleanup()

btn.on_backspace = btnstop

"""
Attach leftMotor to cSensorLeft and rightMotor to cSensorRight.
If the value of either sensor is above _threshold stop the respective
motor, otherwise set speed of motor to intensity * _amplify.
Hit back button to stop program.
"""
try:
    while True:
        btn.process()

        leftIntensity = cSensorLeft.value()
        rightIntensity = cSensorRight.value()

        if leftIntensity > _threshold:
            motorLeft.run_forever(speed_sp=0)
        else:
            lSpeed = _maxIntensity - leftIntensity
            motorLeft.run_forever(speed_sp=lSpeed*_amplify)

        if rightIntensity > _threshold:
            motorRight.run_forever(speed_sp=0)
        else:
            rSpeed = _maxIntensity - rightIntensity
            motorRight.run_forever(speed_sp=rSpeed*_amplify)
finally:
    cleanup()
