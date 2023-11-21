import Motor
import wpilib

class TalonMotor(Motor.Motor):
    def __init__(self,channel):
        super().__init__()
        self.motor_reference = wpilib.Talon(channel)