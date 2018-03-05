#!/usr/bin/env python3
from Robot import Robot

"""
Coward is based on Braitenberg's vehicle 2A.
It should 'become restless in the vicinity of sources
avoiding them, escaping until it safely reaches a place
where the influence of the source is scarcely felt.' 
(Braitenberg, 1987)
"""

robot = Robot(50)

btn = robot.getButtons()

leftMotor = robot.getMotor('left')
rightMotor = robot.getMotor('right')

def btnStop(b) -> None:
    """
    Stop the motors and exit the program.

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
