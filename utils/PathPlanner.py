class PathPlanner:
    def __init__(self, keyframes: dict):
        self._keyframes = keyframes
        self.current_speed = 0

    def calculate(position_one: dict, position_two: dict, speed: float):
        f = lambda o, t: (t - o) / speed
        return {
            "x": f(position_one["x"], position_two["x"]),
            "y": f(position_one["y"], position_two["y"]),
            "z": f(position_one["z"], position_two["z"]),
        }

    def run(self):
        for keyframe, next_keyframe in self._keyframes:
            delta_time = keyframe["frame_time"] + next_keyframe["frame_time"]
            length = self.calculate(
                keyframe["position"], 
                next_keyframe["frame_time"], 
                delta_time
            )
            print(length)