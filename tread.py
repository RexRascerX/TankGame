# Class for transportation

def locomotion:
  def __init__(self, speed, powerCost, armorBonus, turnSpeed) :
    self.speed = speed
    self.powerCost = powerCost
    self.armorBonus = armorBonus
    self.turnSpeed = turnSpeed
  def __str__(self):
    return "Locomotion"


def wheels(locomotion):
  def __init__(self, level):
    super().__init__(10*level, 1*level, 2*level, 2*level)
  def __str__(self):
    return "Wheel"
  def armorBonus():
    return 1

def track(locomation):
  def __init__(self, level):
    super().__init__(1*level, 2*level, 6*level, 4*level)
  def __str__(self):
    return "Track"
