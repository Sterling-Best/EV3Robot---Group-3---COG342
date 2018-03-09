#!/usr/bin/env python3
from Robot import Robot

"""
Coward is based on Braitenberg's vehicle 2A.
It should 'become restless in the vicinity of sources
avoiding them, escaping until it safely reaches a place
where the influence of the source is scarcely felt.' 
(Braitenberg, 1987)
"""

<<<<<<< HEAD
_amplify = 10

motorLeft = ev3.LargeMotor('outA')
motorRight = ev3.LargeMotor('outD')
=======
robot = Robot(50)
>>>>>>> simpleBots

btn = robot.getButtons()

leftMotor = robot.getMotor('left')
rightMotor = robot.getMotor('right')

<<<<<<< HEAD
cSensorLeft.mode = 'COL-AMBIENT'
cSensorRight.mode = 'COL-AMBIENT'

#Fucntions
def cleanup() -> None:
    """
    Stop all motors.

    Returns:
        None: Stops Ev3's Motors
=======
def btnStop(b) -> None:
    """
    Stop the motors and exit the program.

    Args:
        b:

    Returns:
        None: Stops motors and exits.
>>>>>>> simpleBots
    """
    robot.stopMotors()
    exit()

<<<<<<< HEAD
def btnstop(a_b) -> None:
    #TODO: Complete Docstring
    """

    Args:
        a_b ():

    Returns:
        None:
    """
    cleanup()

#Declaring button commands
btn.on_backspace = btnstop

#Instructions Execution
"""
Attach leftMotor to leftSensor and rightMotor to rightSensor.
Set the speed of each motor to the value of the intensity * _amplify.
Hit the back button to stop the program.
"""
try:
    while True:
        btn.process()

        leftSpeed = cSensorLeft.value() * _amplify
        rightSpeed = cSensorRight.value() * _amplify

        motorLeft.run_forever(speed_sp=leftSpeed)
        motorRight.run_forever(speed_sp=rightSpeed)
finally:
    cleanup()
=======
btn.on_backspace = btnStop

def run() -> None:
    """
    Attach leftMotor to leftSensor and rightMotor to rightSensor.
    Set the speed of each motor to the value of the intensity * _amplify.
    Hit the back button to stop the program.

    Returns:
        None: continously run the robot, and check for button press.
    """
    try:
        while True:
            btn.process()

            robot.speedUp(leftMotor, robot.getSensorValue('left'))
            robot.speedUp(rightMotor, robot.getSensorValue('right'))
    finally:
        robot.stopMotors()


if __name__ == "__main__":
    run()
>>>>>>> simpleBots
