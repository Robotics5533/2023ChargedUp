import wpilib
import wpilib.drive
import ntcore
from Drive.driveClass import Drive
from constants import *
from utils.math import calculate_direction
import ctre


class Dani(wpilib.TimedRobot):
    def robotInit(self):
        """
        This function is called upon program startup and
        should be used for any initialization code.
        """
        # self.motor1 = ctre.WPI_TalonSRX(1)
        # self.drive.setExpiration(0.2)
        # self.drive.setSafetyEnabled(True)
        # self.drive.feed()
        self.drive = Drive("tank")


    def autonomousInit(self):
        """This function is run once each time the robot enters autonomous mode."""
        self.timer.reset()
        self.timer.start()

    def autonomousPeriodic(self):
        """This function is called periodically during autonomous."""
        if self.timer.get() < 2.0:
            self.drive.arcadeDrive(-0.5, -0.5)
              # Drive forwards at half speed
        else:
            self.drive.arcadeDrive(0, 0)
              # Stop robot

    def teleopPeriodic(self):
        """This function is called periodically during operator control."""
        x, y, z = self.stick.getX(), self.stick.getY(), self.stick.getZ(), 
        self.drive.move(x, y, z)
     
if __name__ == "__main__":
    wpilib.run(Dani)