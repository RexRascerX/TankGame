# Class for transportation

# This is the inheritance class, please make the types below this class.
class locomotion:
  def __init__(self, speed, powerCost, armorBonus, turnSpeed) :
    self.speed = speed
    self.powerCost = powerCost
    self.armorBonus = armorBonus
    self.turnSpeed = turnSpeed
  def __str__(self):
    return "Locomotion"

# Basic mode of transportaion.
# Fast, but not strong.
class wheels(locomotion):
  def __init__(self, level):
    super().__init__(10*level, 1*level, 2*level, 2*level)
  def __str__(self):
    return "Wheel"

# Slightly advanced mode of transportation.
# Slow, but well armored.
class track(locomotion):
  def __init__(self, level):
    super().__init__(1*level, 2*level, 6*level, 4*level)
  def __str__(self):
    return "Track"
