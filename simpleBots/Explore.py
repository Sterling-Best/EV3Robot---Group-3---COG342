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

<<<<<<< HEAD
cSensorLeft.mode = 'COL-AMBIENT'
cSensorRight.mode = 'COL-AMBIENT'

#Functions
def cleanup() -> None:
    """
    Stop all motors.

    Returns:
        None: Stops Ev3's motors
=======
def btnStop(b):
    """
    Stop the motors and exit program.

    Args:
        b:

    Returns:
        None: stops motor and exits.
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
Attach leftMotor to cSensorLeft and rightMotor to cSensorRight.
If the value of either sensor is above _threshold implement Coward,
otherwise implement Aggressive.
Hit back button to stop program.
"""
try:
    while True:
        btn.process()

        leftIntensity = cSensorLeft.value()
        rightIntensity = cSensorRight.value()

        if leftIntensity > _threshold or rightIntensity > _threshold:
            motorLeft.run_forever(speed_sp=rightIntensity*_amplify)
            motorRight.run_forever(speed_sp=leftIntensity*_amplify)
        else:
            lSpeed = _maxIntensity - leftIntensity
            rSpeed = _maxIntensity - rightIntensity
            motorLeft.run_forever(speed_sp=lSpeed*_amplify)
            motorRight.run_forever(speed_sp=rSpeed*_amplify)
finally:
    cleanup()
=======
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
>>>>>>> simpleBots
