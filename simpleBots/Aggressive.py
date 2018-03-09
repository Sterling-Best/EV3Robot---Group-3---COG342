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

<<<<<<< HEAD
#Functions
def cleanup() -> None:
    """
    Stop all motors.

    Returns:
        None: Stops Ev3's motors.
=======
    Returns:
        None: Stops motors and exits.
>>>>>>> simpleBots
    """
    robot.stopMotors()
    exit()

<<<<<<< HEAD
def btnstop(a_b) -> None:
    #TODO: Finish Doctstring
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
Attach leftMotor to cSensorRight and rightMotor to cSensorLeft.
Set speed of each motor to the value of the intensity * _amplify.
Hit back button to stop program.
"""
try:
    while True:
        btn.process()

        leftSpeed = cSensorRight.value() * _amplify
        rightSpeed = cSensorLeft.value() * _amplify

        motorLeft.run_forever(speed_sp=leftSpeed)
        motorRight.run_forever(speed_sp=rightSpeed)
finally:
    cleanup()
=======
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
>>>>>>> simpleBots
