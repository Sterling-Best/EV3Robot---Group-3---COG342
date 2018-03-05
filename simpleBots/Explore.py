#!/usr/bin/env python3
from Robot import Robot

"""
Explore is based on Braitenberg's vehicle 3B.
'It likes the nearby source all right, but keeps an eye
open for other, perhaps stronger sources.' (Braitenberg, 1987)
"""

__threshold = 20

robot = Robot(50)

leftMotor = robot.getMotor('left')
rightMotor = robot.getMotor('right')

btn = robot.getButtons()

def btnStop(b):
    """
    Stop the motors and exit program.

    Args:
        b:

    Returns:
        None: stops motor and exits.
    """
    robot.stopMotors()
    exit()

btn.on_backspace = btnStop

def run() -> None:
    """
    Attach leftMotor to cSensorLeft and rightMotor to cSensorRight.
    If the value of either sensor is above _threshold implement Coward,
    otherwise implement Aggressive.
    Hit back button to stop program.

    Returns:
        None: continously run the robot and check for button press.
    """
    try:
        while True:
            btn.process()

            leftIntensity = robot.getSensorValue('left')
            rightIntensity = robot.getSensorValue('right')

            if leftIntensity > __threshold or rightIntensity > __threshold:
                robot.speedUp(leftMotor, leftIntensity)
                robot.speedUp(rightMotor, rightIntensity)
            else:
                robot.slowDown(leftMotor, leftIntensity)
                robot.slowDown(rightMotor, rightIntensity)
    finally:
        robot.stopMotors()

if __name__ == "__main__":
    run()
