import wpilib
import wpilib.drive


class Dani(wpilib.TimedRobot):
    def robotInit(self):
        """
        This function is called upon program startup and
        should be used for any initialization code.
        """
        self.spark = wpilib.Spark(1)
        self.sparkt = wpilib.Spark(0)
        self.stick = wpilib.Joystick(0)
        self.timer = wpilib.Timer()

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
        # self.right_motor.set(1)
        # self.left_motor.set(1)
        #self.drive.arcadeDrive(self.stick.getY(), self.stick.getX())
        speed = self.stick.getY()
        self.spark.set(speed)
        self.sparkt.set(speed)
        print(f"x:{self.stick.getX()} y:{self.stick.getY()}")


if __name__ == "__main__":
    wpilib.run(Dani)