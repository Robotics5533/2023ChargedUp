import ntcore


class UwUlimelight:
    def __init__(self) -> None:
        self.ntinst = ntcore.NetworkTableInstantce.getDefault()
        self.limelight_ntable = self.ntinst.getTable('limelight')
        