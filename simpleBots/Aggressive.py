#! /usr/bin/evn python3
import ev3dev.ev3 as ev3

"""
Aggressive is an algorithm based on Braitenberg's vehivle 2B.
It should be 'excited by the presence of sources, but resolutely
turn towards them and hit them with high velocity, as if it wanted
to destroy them.' (Braitenberg, 1987)
"""

_amplify = 100

motorLeft = ev3.LargeMotor('outA')
motorRight = ev3.LargeMotor('outB')

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
Attach leftMotor to cSensorRight and rightMotor to cSensorLeft.
Set speed of each motor to the value of the intensity each sensor
is detecting.
Hit back button to stop program.
"""
try:
    while True:
        btn.process()
        
        leftSpeed = cSensorRight.value() * _amplify
        rightSpeed = cSensorLeft.value() * _amplify

        motorLeft.run_forever(speed_sp=leftSpeed)
        motorRight.run_forever(spped_sp=rightSpeed)

except KeyboardInterrupt:
    pass
finally:
    cleanUp()
