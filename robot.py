import wpimath
import wpilib
import wpilib.drive
import cv2
import numpy as np
from networktables import NetworkTables
import ntcore

class Dani(wpilib.TimedRobot):
    
    def robotInit(self):
        """
        This function is called upon program startup and
        should be used for any initialization code.
        """
        self.can = wpilib.Talon()
        self.spark = wpilib.Spark(0)
        self.sparkt = wpilib.Spark(1)
        self.stick = wpilib.Joystick(0)
        self.timer = wpilib.Timer()
        self.ntinst = ntcore.NetworkTableInstance.getDefault()
        self.limelightnt = self.ntinst.getTable('limelight')
        
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
        # self.right_motor.set(1)
        # self.left_motor.set(1)
        #self.drive.arcadeDrive(self.stick.getY(), self.stick.getX())
        speed = self.stick.getY()
        if speed != 0 and self.stick.getRawButtonPressed(1):
            signum = speed / abs(speed)
            speed = (speed * speed) * signum
        else:  
            self.spark.set(speed)
            self.sparkt.set(speed)
        
        justpressed = self.stick.getRawButtonPressed(1)
        pressed = self.stick.getRawButton(1)
        # inst = ntcore.NetworkTableInstance.getDefault()
        # table = inst.getTable("limelight")
        table = self.limelightnt

        tx = table.getNumber('tx',None)
        ty = table.getNumber('ty',None)
        ta = table.getNumber('ta',None)
        ts = table.getNumber('ts',None)
        tl = table.getNumber('tl',"lol fail")
        tlong = table.getNumber('tlong', "stupid face stupid")
        
        print(tx,ty,ta,ts,tl,tlong)
        print(table.getKeys())

        print(f"x:{self.stick.getX()} y:{self.stick.getY()}")
        self.limelightnt.putNumber('ledMode', 3 if pressed else 1)
        # print(inst.getTable("limelight").getNumber('ledMode', "lol nothin"))
        # inst.getTable("limelight").putNumber('ledMode',0)
        # print(inst.getTable("limelight").getNumber('ledMode', "lol still nothin"))
        print("\n\n")
        

    # runPipeline() is called every frame by Limelight's backend.
    # def runPipeline(image):
    #     # convert the input image to the HSV color space
    #     img_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    #     # convert the hsv to a binary image by removing any pixels
    #     # that do not fall within the following HSV Min/Max values
    #     img_threshold = cv2.inRange(img_hsv, (60, 70, 70), (85, 255, 255))

    #     # find contours in the new binary image
    #     contours, _ = cv2.findContours(img_threshold,
    #     cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    #     largestContour = np.array([[]])

    #     # initialize an empty array of values to send back to the robot
    #     llpython = [0,0,0,0,0,0,0,0]

    #     # if contours have been detected, draw them
    #     if len(contours) > 0:
    #         cv2.drawContours(image, contours, -1, 255, 2)
    #         # record the largest contour
    #         largestContour = max(contours, key=cv2.contourArea)

    #         # get the unrotated bounding box that surrounds the contour
    #         x,y,w,h = cv2.boundingRect(largestContour)

    #         # draw the unrotated bounding box
    #         cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,255),2)

    #         # record some custom data to send back to the robot
    #         llpython = [1,x,y,w,h,9,8,7]

    #     #return the largest contour for the LL crosshair, the modified image, and custom robot data
    #     return largestContour, image, llpython

if __name__ == "__main__":
    wpilib.run(Dani)