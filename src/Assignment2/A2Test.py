from Robot import Robot
from Ev3Global import Ev3Global
from Ev3Coordinates import Ev3Coordinates



globalGrid = Ev3Global(16)

#Robot Parts
robot = Robot(10)
leftMotor = robot.getMotor('left')
rightMotor = robot.getMotor('right')
leftSensor = robot.cSensorRight
leftSensor.setMode(1,2)
rightSensor = robot.cSensorLeft
rightSensor.setMode(4,2)
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
        if leftSensor.ReadRawValue(1,0) > 1:
            globalGrid.addcoord(Ev3Coordinates(0,0,"Color_black"))
            robot.speedUp(leftMotor, 20)
        if rightSensor.ReadRawValue(4,0) > 6:
            globalGrid.addcoord(Ev3Coordinates(0,0,"Color_white"))
            robot.speedUp(rightMotor, 20)
    globalGrid.exportcsv()
        #robot.speedUp(leftMotor, 10)
        #robot.speedUp(rightMotor, 10)
