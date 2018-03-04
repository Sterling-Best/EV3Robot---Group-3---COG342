#! /usr/bin/env python3
import ev3dev.ev3 as ev3

"""
Coward is an algorithm based on Braitenberg's vehicle 2A.
It should 'become restless in the vicinity of sources
avoiding them, escaping until it safely reaches a place
where the influence of the source is scarcely felt.' 
(Braitenberg, 1987)
"""
    
motorLeft = ev3.LargeMotor('outA')
motorRight = ev3.LargeMotor('outD')

colorSensorA = ev3.ColorSensor()
assert colorSensorA.connected
colorSensorB = ev3.ColorSensor()
assert colorSensorB.connected


btn = ev3.Button()

colorSensorA.mode = 'COL-AMBIENT'
colorSensorB.mode = 'COL-AMBIENT'

print(colorSensorA.address)
print(colorSensorB.address)

def cleanUp():
    """
    Stop all motors.
    """
    motorLeft.stop()
    motorRight.stop()
    exit()

def btnStop(b):
    cleanUp()

btn.on_backspace = btnStop


"""
Attach leftMotor to leftSensor and rightMotor to rightSensor.
Set the speed of each motor to the value of the intensity each
sensor is detecting.
Hit the back button to stop the program.
"""
try:
    while True:
        btn.process()
        
        leftSpeed = s1.value()
        rightSpeed = s4.value()
        
        motorLeft.run_forever(speed_sp=leftSpeed)
        motorRight.run_forever(speed_sp=rightSpeed)

except KeyboardInterrup:
    pass
finally:
    cleanUp()
