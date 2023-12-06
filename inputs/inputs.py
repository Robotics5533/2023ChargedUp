inputmap = {
}
def is_action(action):
    for event in inputmap[action]:
        if event.getValue(): return True
    return False
class Inputs:
    def getValue():
        return False
class JoyInput(Inputs):
    pass 
    def __init__(self, joystick, button) -> None:
        super().__init__()
        self.joystick = joystick
        self.button = button
    def getValue(self):
        return self.joystick.getRaw(self.button)