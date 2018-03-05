#!/usr/bin/env python3
from Robot import Robot

"""
Aggressive is based on Braitenberg's vehicle 2B.
It should be 'excited by the presence of sources, but resolutely
turn towards them and hit them with high velocity, as if it wanted
to destroy them.' (Braitenberg, 1987)
"""

robot = Robot(50)

btn = robot.getButtons()

leftMotor = robot.getMotor('left')
rightMotor = robot.getMotor('right')

def btnStop(b):
    """
    Stop the motors and exit program.

    Args:
        b:

    Returns:
        None: Stops motors and exits.
    """
    robot.stopMotors()
    exit()

btn.on_backspace = btnStop

def run() -> None:
    """
    Attach leftMotor to cSensorRight and rightMotor to cSensorLeft.
    Set speed of each motor to the value of the intensity * _amplify.
    Hit back button to stop program.

    Returns:
        None: continously run the robot, and check for button press.
    """
    try:
        while True:
            btn.process()

            robot.speedUp(leftMotor, robot.getSensorValue('right'))
            robot.speedUp(rightMotor, robot.getSensorValue('left'))
    finally:
        robot.stopMotors()

if __name__ == "__main__":
    run()
