import wpilib
import wpilib.drive
from wpilib.drive import DifferentialDrive
import ntcore
from constants import *
from utils.math import calculate_direction
import ctre


class Dani(wpilib.TimedRobot):
    def robotInit(self):
        """
        This function is called upon program startup and
        should be used for any initialization code.
        """
        self.timer = wpilib.Timer()
        self.frontLeft = wpilib.Talon(Robot.controllers.motors.front.left)
        self.rearLeft = wpilib.Talon(Robot.controllers.motors.rear.left)
        self.frontRight = wpilib.Talon(Robot.controllers.motors.front.right)
        self.rearRight = wpilib.Talon(Robot.controllers.motors.rear.right)
        self.left = wpilib.MotorControllerGroup(self.frontLeft, self.rearLeft)
        self.right = wpilib.MotorControllerGroup(self.frontRight, self.rearRight)
        self.drive = DifferentialDrive(self.left, self.right)
        self.drive.setExpiration(0.4)
        self.stick = wpilib.Joystick(Robot.controllers.driver.joystick)
        self.motor1 = ctre.WPI_TalonSRX(1)
        # self.ntinst = ntcore.NetworkTableInstance.getDefault()
        # self.limelightnt = self.ntinst.getTable('limelight')
        # self.__nt = NetworkTables.getTable("limelight")

    def autonomousInit(self):
        """This function is run once each time the robot enters autonomous mode."""
        self.timer.reset()
        self.timer.start()

    def autonomousPeriodic(self):
        """This function is called periodically during autonomous."""
        if self.timer.get() < 2.0:
            self.drive.arcadeDrive(-0.5, -0.5)  # Drive forwards at half speed
        else:
            self.drive.arcadeDrive(0, 0)  # Stop robot

    def teleopPeriodic(self):
        """This function is called periodically during operator control."""
        #x, y, z = self.stick.getX(), self.stick.getY(), self.stick.getZ(), 
        #self.drive.tankDrive(calculate_direction(1, x, y, z), calculate_direction(0, x, y, z))
        self.motor1.set(0.5)


if __name__ == "__main__":
    wpilib.run(Dani)
