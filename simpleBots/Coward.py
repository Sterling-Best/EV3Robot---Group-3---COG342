#!/usr/bin/env python3
from ev3dev.ev3 as ev3

"""
Coward is an algorithm based on Braitenberg's vehicle 2A.
It should 'become restless in the vicinity of sources
avoiding them, escaping until it safely reaches a place
where the influence of the source is scarcely felt.' 
(Braitenberg, 1987)
"""
    
self.leftMotor = ev3.LargeMotor('outA')
self.rightMotor = ev3.LargeMotor('outD')
self.leftSensor = ev3.ColorSensor('out1')
self.rightSensor = ev3.ColorSensor('out4')

self.leftMotor.run_forever(speed_sp = 0)
self.rightMotor.run_forever(speed_sp = 0)
self.leftSensor.mode = 'COL-AMBIENT'
self.rightSensor.mode = 'COL-AMBIENT'


"""
Attach leftMotor to leftSensor and rightMotor to rightSensor.
Set the speed of each motor to the value of the intensity each
sensor is detecting.
Hit the back button to stop the program.
"""
exitBtn = Button()

while exitBtn.on_backspace() == False:
    leftMotor.speed_sp = leftSensor.value()
    rightMotor.speed_sp = rightSensor.value()

leftMotor.stop()
rightMotor.stop()
