import time
import math

from Robot import Robot
from Ev3Global import Ev3Global
from Ev3Coordinates import Ev3Coordinates



globalGrid = Ev3Global(16)

#Robot Parts
robot = Robot(10)
leftMotor = robot.getMotor('left')
rightMotor = robot.getMotor('right')
#leftSensor = robot.cSensorRight
#leftSensor.mode = 'COL-COLOR'
#rightSensor = robot.cSensorLeft
#rightSensor.mode = 'COL-COLOR'
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
    # for x in range(360):
    #     robot.tankrotate(1)
    #
    # time.sleep(5)

    robot.LCD.clear()
    robot.LCD.update()
    for x in range(36):
        distance = robot.ultrasonic.value()/10 + 2.5
        x = distance * math.sin(robot.get_currentdegrees())
        y = distance * math.cos(robot.get_currentdegrees())
        robot.globalGrid.addcoord(Ev3Coordinates(x,y,"PointOfObstruction"))
        robot.tankrotate(10)
    robot.LCD.clear()
    robot.lcddrawglobal()
    robot.LCD.update()
    globalGrid.exportcsv()


    # movefowardtest(1)
    # movefowardtest(5)

    # teststr = ["motorprecisiontest1"]
    # testbool = True
    # while True:
    #     btn.process()
    #     if "motorprecisiontest1" in teststr:
    #        testbool = motorprecisiontest1(testbool)


    #     if leftSensor.color  == 6 :
    #         globalGrid.addcoord(Ev3Coordinates(0,0,"Color_black"))
    #         robot.speedUp(leftMotor, 5)
    #     if rightSensor.color == 1:
    #         globalGrid.addcoord(Ev3Coordinates(0,0,"Color_white"))
    #         robot.speedUp(rightMotor, 5)
    # globalGrid.exportcsv()
        #robot.speedUp(leftMotor, 10)
        #robot.speedUp(rightMotor, 10)

def motorprecisiontest1 (test: bool) -> bool:
    if test == True:
        leftMotor.run_to_rel_pos(speed_sp=200, position_sp=75)
        leftMotor.wait_while(leftMotor.STATE_RUNNING)
        return False
    else:
        rightMotor.run_to_rel_pos(speed_sp=200, position_sp=75)
        rightMotor.wait_while(rightMotor.STATE_RUNNING)
        return True

def movefowardtest(distance):
    robot.moveforward(distance)
    time.sleep(5)


#def motorcmtest():


