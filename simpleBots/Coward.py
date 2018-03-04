#!/usr/bin/env python3
from ev3dev.ev3 as ev3

"""
Coward is an algorithm based on Braitenberg's vehicle 2A.
It should 'become restless in the vicinity of sources
avoiding them, escaping until it safely reaches a place
where the influence of the source is scarcely felt.' 
(Braitenberg, 1987)
"""
    
leftMotor = ev3.LargeMotor('outA')
rightMotor = ev3.LargeMotor('outD')
leftSensor = ev3.ColorSensor('out1')
rightSensor = ev3.ColorSensor('out4')

leftMotor.run_forever(speed_sp = 0)
rightMotor.run_forever(speed_sp = 0)
leftSensor.mode = 'COL-AMBIENT'
rightSensor.mode = 'COL-AMBIENT'


"""
Attach leftMotor to leftSensor and rightMotor to rightSensor.
Set the speed of each motor to the value of the intensity each
sensor is detecting.
Hit the back button to stop the program.
"""
btn = ev3.Button()

while True:
    if btn.any(): 
        break
    else: 
        leftMotor.speed_sp = leftSensor.value()
        rightMotor.speed_sp = rightSensor.value()

leftMotor.stop()
rightMotor.stop()
