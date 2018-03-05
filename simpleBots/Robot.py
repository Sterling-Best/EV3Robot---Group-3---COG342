import ev3dev.ev3 as ev3

class Robot:
    """
    """

    _amplify: int
    _threshold = 20
    _maxIntensity = 50

    motorLeft = ev3.LargeMotor('outA')
    motorRight = ev3.LargeMotor('outD')

    cSensorLeft = ev3.ColorSensor('in1')
    cSensorRight = ev3.ColorSensor('in4')

    def __init__(self, amplify: int) -> None:
        """
        """
        self._amplify = amplify
    
    def speedUp(self, motor: str, speed: int) -> None:
        """
        """
        motorSpeed = speed * _amplify
        if motor == 'left':
            motorLeft.run_forever(speed_sp = speed * _amplify)
        else:
            motorRight.run_forever(speed_sp = speed * _amplify)
        
    def slowDown(self, motor: str, speed: int) -> None:
        """
        """
        motorSpeed = ( _max_intensity - speed) * _amplify
        if motor == 'left':
            motorLeft.run_forever(speed_sp=motorSpeed)
        else:
            motorRight.run_forever(speed_sp=motorSpeed)
    
    def getSensorValue(self, sensor: str) -> int:
        """
        """
        if sensor == 'left':
            return cSensorLeft.value() 
        else:
            return cSensorRight.value()

    def stopMotors(self) -> None:
        """
        """
        motorLeft.stop()
        motorRight.stop()

    def __str(self) -> str:
        """
        Generates string representation of Robot
        
        Returns:
            str: String representation of Robot
        """
        return "Amplifying motors by " + _amplify + ". Max Intensity: " + _maxIntensity + ". Threshold: " + _threshold + "."    
