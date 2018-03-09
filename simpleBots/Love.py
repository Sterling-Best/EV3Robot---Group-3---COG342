#!/usr/bin/env python3
from Robot import Robot

"""
Love is based on Braitenberg's vehicle 3A.
It will 'stay close by in quiet admiration from the time
it spots the source to all future time.' (Braitenberg, 1987)
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
        None: Stops Ev3's Motors
=======
def btnStop(b):
    """
    Stop the motors and exit program

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

#Declaring button comands
btn.on_backspace = btnstop

#Instructions Exectuion
"""
Attach leftMotor to cSensorLeft and rightMotor to cSensorRight.
If the value of either sensor is above _threshold stop the respective
motor, otherwise set speed of motor to intensity * _amplify.
Hit back button to stop program.
"""
try:
    while True:
        btn.process()

        leftIntensity = cSensorLeft.value()
        rightIntensity = cSensorRight.value()

        if leftIntensity > _threshold:
            motorLeft.run_forever(speed_sp=0)
        else:
            lSpeed = _maxIntensity - leftIntensity
            motorLeft.run_forever(speed_sp=lSpeed*_amplify)

        if rightIntensity > _threshold:
            motorRight.run_forever(speed_sp=0)
        else:
            rSpeed = _maxIntensity - rightIntensity
            motorRight.run_forever(speed_sp=rSpeed*_amplify)
finally:
    cleanup()
=======
btn.on_backspace = btnStop

def run() -> None:
    """
    Attach leftMotor to cSensorLeft and rightMotor to cSensorRight.
    If the value of either sensor is above _threshold stop the respective
    motor, otherwise set speed of motor to intensity * _amplify.
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
                robot.stopMotors()
            else:
                robot.slowDown(leftMotor, leftIntensity)
                robot.slowdown(rightMotor, rightIntensity)

    finally:
        robot.stopMotors()

if __name__ == "__main__":
    run()
>>>>>>> simpleBots
