import wpilib
import wpilib.drive
from driveClass import UwUTankDrive, UwUMecanumDrive
from PathPlanner import PathPlanner
from constants import *


class Dani(wpilib.TimedRobot):
    def robotInit(self):

        # This function is called upon program startup and
        # should be used for any initialization code.

        self.drive = UwUMecanumDrive(1, 2, 3, 4)
        self.PathPlanner = PathPlanner(
            {
                "keyframes": [
                    {
                        "frame_time": 0,
                        "position": {
                            "x": 0,
                            "y": 0,
                            "z": 0,
                        },
                    },
                    {
                        "frame_time": 2,
                        "position": {
                            "x": 1,
                            "y": 1,
                            "z": 1,
                        },
                    },
                ]
            }
        )
        # self.drive = UwUTankDrive([wpilib.Talon(1)], [wpilib.Talon(0)])
        self.stick = wpilib.Joystick(0)

    def autonomousInit(self):
        # This function is run once each time the robot enters autonomous mode.
        self.timer.reset()
        self.timer.start()
        self.PathPlanner.run()

    def autonomousPeriodic(self):
        # This function is called periodically during autonomous.
        if self.timer.get() < 2.0:
            self.drive.move(self.stick.getRawAxis(0), self.stick.getRawAxis(1))
            # Drive forwards at half speed
        else:
            self.drive.move(0, 0)
            # Stop robot

    def teleopPeriodic(self):
        # This function is called periodically during operator control.
        x, y, z = (
            self.stick.getX(),
            self.stick.getY(),
            self.stick.getZ(),
        )
        self.drive.move(x, y, z)


if __name__ == "__main__":
    wpilib.run(Dani)
