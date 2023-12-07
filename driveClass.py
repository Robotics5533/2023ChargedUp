import ctre
import wpilib
#from wpilib.drive import DifferentialDrive


class UwUDrive:
    def drive(self):
        pass


class UwUTankDrive:

#abc
    def __init__(self, left_motors: [], right_motors: []):
        
        
        self.left_motors = left_motors
        self.right_motors = right_motors
        
        
        for i in range(len(self.left_motors)):
            self.__dict__[f"left_motor_{i + 1}"] = self.left_motors[i]
            
        for i in range(len(self.right_motors)):
            self.__dict__[f"right_motor_{i + 1}"] = self.right_motors[i]



        # for left_motor in left_motors:
        #     self.__dict__[f"left_motor_{left_motor + 1}"] = wpilib.Talon(left_motor)
        
        
        # for right_motor in right_motors:
        #     self.__dict__[f"right_motor_{right_motor - 1}"] = wpilib.Talon(right_motor)
            
            
        # self.left = wpilib.MotorControllerGroup(self.left_motor_1, self.left_motor_2)
        # self.right = wpilib.MotorControllerGroup(self.right_motor_1, self.right_motor_2)
        #self.drive = DifferentialDrive(self.left, self.right)


    @staticmethod
    def calculate_direction(type: int, x: int, y: int, z: int) -> int:
        if type == 0:
            return -(x + -y + z)
        else:
            return (x + y + z)
    
    
    def move(self, x: int, y: int, z: int = 0):
        for motor in self.left_motors:
            motor.set(self.calculate_direction(1, x, y, z))
        for motor in self.right_motors:
            motor.set(self.calculate_direction(0, x, y, z))

class UwUMecanumDrive:



    def __init__(self, top_left: int, top_right: int, bottom_left: int, bottom_right: int):
        self.top_left_motor = ctre.WPI_TalonSRX(top_left)
        self.top_right_motor = ctre.WPI_TalonSRX(top_right)
        self.bottom_left_motor = ctre.WPI_TalonSRX(bottom_left)
        self.bottom_right_motor = ctre.WPI_TalonSRX(bottom_right)


    def move(self, x: int, y: int, z: int):
        self.top_left_motor.set(-x + y + z)
        self.top_right_motor.set(x + y - z)
        self.bottom_left_motor.set(x + y + z)
        self.bottom_right_motor.set(-x + y - z)

        # self.drive.setExpiration(0.2)
        # self.drive.setSafetyEnabled(True)
        # self.drive.feed()