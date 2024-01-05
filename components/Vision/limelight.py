import ntcore


class UwUlimelight:
    def __init__(self):
        self.ntinst = ntcore.NetworkTableInstance.getDefault()
        self.limelight_ntable = self.ntinst.getTable('limelight')

    def get_limelight_arg(self, channel: str, default_value: int):
        return self.limelight_ntable.getNumber(channel, default_value)

    def getoffsetUwU(self):
        if not self.get_limelight_arg("tv", 0):
            return [0, 0, 0]
        else:
            return [self.get_limelight_arg("tx", 0), self.get_limelight_arg("ty", 0), 0]
