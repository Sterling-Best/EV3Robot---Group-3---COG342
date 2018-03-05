#!/usr/bin/env python3
import ev3dev.ev3 as ev3
import Robot

"""
Coward is based on Braitenberg's vehicle 2A.
It should 'become restless in the vicinity of sources
avoiding them, escaping until it safely reaches a place
where the influence of the source is scarcely felt.' 
(Braitenberg, 1987)
"""

robot = Robot(50)


def btnStop(b):
    robot.stopMotors()
    exit()

btn.on_backspace = btnStop


"""
Attach leftMotor to leftSensor and rightMotor to rightSensor.
Set the speed of each motor to the value of the intensity * _amplify.
Hit the back button to stop the program.
"""
try:
    while True:
        btn.process()
        
        robot.speedUp('left', robot.getSensorValue('left'))
        robot.speedUp('right', robot.getSensorValue('right'))
finally:
    cleanUp()
