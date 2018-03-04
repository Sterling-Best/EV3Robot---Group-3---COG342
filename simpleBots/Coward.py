#! /usr/bin/env python3
import ev3dev.ev3 as ev3

"""
Coward is an algorithm based on Braitenberg's vehicle 2A.
It should 'become restless in the vicinity of sources
avoiding them, escaping until it safely reaches a place
where the influence of the source is scarcely felt.' 
(Braitenberg, 1987)
"""
    
mA = ev3.LargeMotor('outA')
mD = ev3.LargeMotor('outD')

s1 = ev3.ColorSensor('out1')
assert s1.connected
s4 = ev3.ColorSensor('out4')
assert s4.connected


btn = ev3.Button()

s1.mode = 'COL-AMBIENT'
s4.mode = 'COL-AMBIENT'

def cleanUp():
    """
    Stop all motors.
    """
    mA.stop()
    mD.stop()
    exit()

def btnStop(b):
    cleanUp()

btn.on_backspace = btnStop


"""
Attach leftMotor to leftSensor and rightMotor to rightSensor.
Set the speed of each motor to the value of the intensity each
sensor is detecting.
Hit the back button to stop the program.
"""
try:
    while True:
        btn.process()
        
        leftSpeed = s1.value()
        rightSpeed = s4.value()
        
        mA.run_forever(speed_sp=leftSpeed)
        mD.run_forever(speed_sp=rightSpeed)

except KeyboardInterrup:
    pass
finally:
    cleanUp()
