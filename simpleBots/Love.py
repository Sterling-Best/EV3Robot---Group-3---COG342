#!/usr/bin/env python3
import ev3dev.ev3 as ev3

"""
Love is based on Braitenberg's vehicle 3A.
It will 'stay close by in quiet admiration from the time
it spots the source to all future time.' (Braitenberg, 1987)
"""

_amplify = 10
_threshold = 20

motorLeft = ev3.LargeMotor('outA')
motorRight = ev3.LargeMotor('outD')

cSensorLeft = ev3.ColorSensor('in1')
cSensorRight = ev3.ColorSensor('in4')

btn = ev3.Button()

cSensorLeft.mode = 'COL-AMBIENT'
cSensorRight.mode = 'COL-AMBIENT'

def cleanUp():
    """
    Stop all motors.
    """
    motorLeft.stop()
    motorRight.stop()
    exit()

def btnStop(b):
    cleanUp()

btn.on_backspace = btnStop

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
            lSpeed = 100 - leftIntensity
            motorLeft.run_forever(lSpeed * _amplify)

        if rightIntensity > _threshold:
            motorRight.run_forever(speed_sp=0)
        else:
            rSpeed = 100 - rightIntensity
            motorRight.run_forever(rSpeed * _amplify)
finally:
    cleanUp()
