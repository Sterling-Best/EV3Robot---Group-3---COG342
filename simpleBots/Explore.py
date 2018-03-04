#!/usr/bin/env python3
import ev3dev.ev3 as ev3

"""
Explore is based on Braitenberg's vehicle 3B.
'It likes the nearby source all right, but keeps an eye
open for other, perhaps stronger sources.' (Braitenberg, 1987)
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
If the value of either sensor is above _threshold implement Coward,
otherwise implement Aggressive.
Hit back button to stop program.
"""
try:
    while True:
        btn.process()
        
        leftIntensity = cSensorLeft.value()
        rightIntensity = cSensorRight.value()
        
        if leftIntensity > _threshold or rightIntensity > _threshold:
            motorLeft.run_forever(rightIntensity * _amplify)
            motorRight.run_forever(leftIntensity * _amplify)
        else:
            lSpeed = 100 - leftIntensity
            rSpeed = 100 - rightIntensity
            motorLeft.run_forever(lSpeed * _amplify)
            motorRight.run_forever(rSpeed * _amplify)
finally:
    cleanUp()
