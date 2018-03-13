from Robot import Robot
from Ev3Global import Ev3Global
from Ev3Coordinates import Ev3Coordinates



globalGrid = Ev3Global(16)

#Robot Parts
robot = Robot(10)
leftMotor = robot.getMotor('left')
rightMotor = robot.getMotor('right')
leftSensor = robot.cSensorRight
leftSensor.mode = 'COL-COLOR'
rightSensor = robot.cSensorLeft
rightSensor.mode = 'COL-COLOR'
btn = robot.getButtons()


def btnStop(b) -> None:
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
    while True:
        btn.process()
        if rightSensor.value(1) > 50:
            globalGrid.addcoord(Ev3Coordinates(0,0,"Color_black"))
            robot.speedUp(leftMotor, 20)
        if rightSensor.value(2) > 50:
            globalGrid.addcoord(Ev3Coordinates(0,0,"Color_white"))
            robot.speedUp(rightMotor, 20)
    globalGrid.exportcsv()
        #robot.speedUp(leftMotor, 10)
        #robot.speedUp(rightMotor, 10)
