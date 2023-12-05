import wpilib
from utils.math import calculate_direction
from wpilib.drive import DifferentialDrive

class Drive:
    def __init__(self, drive_type: str):
        self.drive_type = drive_type
        self.frontLeft = wpilib.Talon(0)
        self.rearLeft = wpilib.Talon(1)
        self.frontRight = wpilib.Talon(2)
        self.rearRight = wpilib.Talon(3)
        self.left = wpilib.MotorControllerGroup(self.frontLeft, self.rearLeft)
        self.right = wpilib.MotorControllerGroup(self.frontRight, self.rearRight)
        self.drive = (
            wpilib.drive.MecanumDrive(
                self.frontLeft, self.rearLeft, self.frontRight, self.rearRight
            )
            if self.drive_type == "mecanum"
            else DifferentialDrive(self.left, self.right)
        )

    def move(self, x: int, y: int, z: int):
        if self.drive_type == "mecanum":
            self.drive.driveCartesian(
                -y,
                -x,
                -z,
            )
        elif self.drive_type == "tank":
            self.drive.tankDrive(
                calculate_direction(1, x, y, z), calculate_direction(0, x, y, z)
            )
