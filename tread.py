# Class for transportation

def locomotion:
  def __init__(self, speed, powerCost, turnSpeed) :
    self.speed = speed
    self.powerCost = powerCost
    self.turnSpeed = turnSpeed
  def __str__(self):
    return "Locomotion"


def wheels(locomotion):
  def __init__(self):
    super().__init__(10, 1, 2)
  def __str__(self):
    return "Wheel"
