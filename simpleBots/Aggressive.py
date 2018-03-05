#!/usr/bin/env python3
import ev3dev.ev3 as ev3

"""
Aggressive is based on Braitenberg's vehicle 2B.
It should be 'excited by the presence of sources, but resolutely
turn towards them and hit them with high velocity, as if it wanted
to destroy them.' (Braitenberg, 1987)
"""

_amplify = 10

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
        None: Stops Ev3's motors.
    """
    motorLeft.stop()
    motorRight.stop()
    exit()

def btnstop(a_b) -> None:
    #TODO: Finish Doctstring
    """

    Args:
        a_b ():

    Returns:
        None:

    """
    cleanup()

btn.on_backspace = btnstop

"""
Attach leftMotor to cSensorRight and rightMotor to cSensorLeft.
Set speed of each motor to the value of the intensity * _amplify.
Hit back button to stop program.
"""
try:
    while True:
        btn.process()

        leftSpeed = cSensorRight.value() * _amplify
        rightSpeed = cSensorLeft.value() * _amplify

        motorLeft.run_forever(speed_sp=leftSpeed)
        motorRight.run_forever(speed_sp=rightSpeed)
finally:
    cleanup()
