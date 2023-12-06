import wpilib
import wpilib.drive
from driveClass import UwUTankDrive
from constants import *
class Dani(wpilib.TimedRobot):
    def robotInit(self):
        """
        This function is called upon program startup and
        should be used for any initialization code.
        """
        self.drive = UwUTankDrive([0, 1], [2, 3])
        self.stick = wpilib.Joystick(0)


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