import ntcore


class UwUlimelight:
    def __init__(self):
        self.ntinst = ntcore.NetworkTableInstance.getDefault()
        self.limelight_ntable = self.ntinst.getTable('limelight')
        #the speed that we are turning correcting rotion by,
        #gets multiplied by rotation factor
        self.turn_direction = 0.1
        #corrective multiple for the turn direction
        #positive numbers get negated, so specify as positive
        #multipys turn direction any time we turn AWAY from the target
        self.rotation_factor = 1


    def apply_turning_error(self, drive):
        start_area = self.get_limelight_arg('ta')
        drive.move(0, 0, self.turn_direction)
        end_area = self.get_limelight_arg('ta')
        if end_area < start_area:
            self.turn_direction *= -self.rotation_factor



    def get_limelight_arg(self, channel: str, default_value: int = 0):
        return self.limelight_ntable.getNumber(channel, default_value)






    def getoffsetUwU(self):
        if not self.get_limelight_arg("tv", 0):
            return [0, 0, 0]
        else:
            return [self.get_limelight_arg("tx"), self.get_limelight_arg("ty"), self.apply_turning_error()]
