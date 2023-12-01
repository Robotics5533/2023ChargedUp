"""
def calculate_direction(type: int, x: int, y: int, z: int) -> int:
    if type == 0:
        return -1 * (-x + -y + z)
    else:
        return (-x + -y + z)
"""
def calculate_direction(type: int, x: int, y: int, z: int) -> int:
    # return -(-x + -y + z) if not type else (-x - y + z)
    if type == 0:
        return -1 * (-x + -y + z)
    else:
        return (-x + -y + z)