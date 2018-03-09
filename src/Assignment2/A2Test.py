from src.Assignment2.Robot import Robot

robot = Robot(10)

leftMotor = robot.getMotor('left')
rightMotor = robot.getMotor('right')



def run() -> None:
    """
    Attach leftMotor to leftSensor and rightMotor to rightSensor.
    Set the speed of each motor to the value of the intensity * _amplify.
    Hit the back button to stop the program.

    Returns:
        None: continously run the robot, and check for button press.
    """
    while robot.getButtons().on_backspace():
        robot.speedUp(leftMotor, 10)
        robot.speedUp(rightMotor, 10)
