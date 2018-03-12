from src.Assignment2.Robot import Robot
from src.Ev3Grid.Ev3Global import Ev3Global

robot = Robot(10)

globalGrid = Ev3Global(16)

leftMotor = robot.getMotor('left')
rightMotor = robot.getMotor('right')

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
        robot.speedUp(leftMotor, 10)
        robot.speedUp(rightMotor, 10)
