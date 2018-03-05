#!/usr/bin/env python3
import ev3dev.ev3 as ev3

class Robot:
    """
    EV3 robot with two motors and two sensors.
    """

    __amplify = 1
    __threshold = 20
    __maxIntensity = 50

    def __init__(self, amplify: int) -> None:
        """
        Set the amount to amplify the motor by, and assign each
        motor and sensor its respective port on the EV3 machine.
        """
        self.__amplify = amplify
        self.motorLeft = ev3.LargeMotor('outA')
        self.motorRight = ev3.LargeMotor('outD')
        self.cSensorLeft = ev3.ColorSensor('in1')
        self.cSensorRight = ev3.ColorSensor('in4')

    def speedUp(self, motor: ev3.LargeMotor, speed: int) -> None:
        """
        Proportionally speed up the motor as speed increases.

        Returns:
            None: calculates and sets speed of motor.
        """
        motorSpeed = speed * self.__amplify
        motor.run_forever(speed_sp=motorSpeed)

    def slowDown(self, motor: ev3.LargeMotor, speed: int) -> None:
        """
        Proportionally slow down the motor as speed increases.

        Returns:
            None: calculates and sets speed of motor.
        """
        motorSpeed = (self.__maxIntensity - speed) * self.__amplify
        motor.run_forever(speed_sp=motorSpeed)

    def getMotor(self, side: str) -> ev3.LargeMotor:
        """
        Identify which motor is on which side and return it.

        Args:
            side (str): string indicating which motor to return.

        Returns:
            ev3.LargeMotor: motor associated with a side of the robot.
        """
        if side == 'left':
            return self.motorLeft
        else:
            return self.motorRight

    def getSensorValue(self, side: str) -> int:
        """
        Read the value of either the left or right sensor.

        Args:
            side (str): string indicating which sensor reading to return.

        Returns:
            int: the value being detected by the sensor.
        """
        if side == 'left':
            return self.cSensorLeft.value()
        else:
            return self.cSensorRight.value()

    def stopMotors(self) -> None:
        """
        Stop both motors.

        Returns:
            None: stops both left and right motor.
        """
        self.motorLeft.stop()
        self.motorRight.stop()

    def getButtons(self) -> ev3.Button:
        """
        Provide access to the EV3 buttons.

        Returns:
            ev3.Button: providing access to the EV3 on board buttons.
        """
        return ev3.Button()

    def __str(self) -> str:
        """
        Generates string representation of Robot

        Returns:
            str: String representation of Robot
        """
        return "Amplifying motors by " + _amplify + ". Max Intensity: " + _maxIntensity + ". Threshold: " + _threshold + "."
