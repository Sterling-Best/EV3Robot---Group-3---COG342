#!/usr/bin/env python3
import ev3dev.ev3 as ev3

class Robot:
    """
    """

    __amplify = 1
    __threshold = 20
    __maxIntensity = 50

    def __init__(self, amplify: int) -> None:
        """
        """
        self.__amplify = amplify
        self.motorLeft = ev3.LargeMotor('outA')
        self.motorRight = ev3.LargeMotor('outD')
        self.cSensorLeft = ev3.ColorSensor('in1')
        self.cSensorRight = ev3.ColorSensor('in4')
    
    def speedUp(self, motor, speed: int) -> None:
        """
        """
        motorSpeed = speed * self.__amplify
        motor.run_forever(speed_sp=motorSpeed)
        
    def slowDown(self, motor, speed: int) -> None:
        """
        """
        motorSpeed = (self.__maxIntensity - speed) * self.__amplify
        motor.run_forever(speed_sp=motorSpeed)

    def getMotor(self, side: str):
        if side == 'left':
            return self.motorLeft
        else:
            return self.motorRight

    
    def getSensorValue(self, sensor) -> int:
        """
        """
        if sensor == 'left':
            return self.cSensorLeft.value() 
        else:
            return self.cSensorRight.value()

    def stopMotors(self) -> None:
        """
        """
        self.motorLeft.stop()
        self.motorRight.stop()

    def getButtons(self):
        """
        """
        return ev3.Button()

    def __str(self) -> str:
        """
        Generates string representation of Robot
        
        Returns:
            str: String representation of Robot
        """
        return "Amplifying motors by " + _amplify + ". Max Intensity: " + _maxIntensity + ". Threshold: " + _threshold + "."    
