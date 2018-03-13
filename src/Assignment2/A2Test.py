from src.Assignment2.Robot import Robot
from src.Ev3Grid.Ev3Global import Ev3Global
from src.Ev3Grid.Ev3Coordinates import Ev3Coordinates



globalGrid = Ev3Global(16)

#Robot Parts
robot = Robot(10)
leftMotor = robot.getMotor('left')
rightMotor = robot.getMotor('right')
leftSensor = robot.getSensorValue('left')
rightSensor = robot.getSensorValue('right')
btn = robot.getButtons()

leftSensor.color = 1

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
        if leftSensor.getSensorValue("left") > 5:
            globalGrid.addcoord(Ev3Coordinates(0,0,"Color_black"))
            robot.speedUp(leftMotor, 20)
            robot.speedUp(rightMotor, 20)

        #robot.speedUp(leftMotor, 10)
        #robot.speedUp(rightMotor, 10)
