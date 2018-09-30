import imaging, numpy
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
  def render(self, x, y, a):
    pass

# Basic mode of transportaion.
# Fast, but not strong.
class wheels(locomotion):
  def __init__(self, level):
    super().__init__(10*level, 1*level, 2*level, 2*level)
    self.length = 14
    self.width = 8
  def __str__(self):
    return "Wheel"
  def numRen(self):
    return 4
  def render(self):
    return imaging.rRect(self.length, self.width, 0x555555)

# Slightly advanced mode of transportation.
# Slow, but well armored.
class track(locomotion):
  def __init__(self, level):
    super().__init__(1*level, 2*level, 6*level, 4*level)
  def __str__(self):
    return "Track"
  def render(self, x, y, a, shiftx, shifty):
    toren = [imaging.rImage(x+shiftx,y+shifty,a,imaging.rRect(8,14,0x111111))]
    toren.append(imaging.rImage(x-shiftx,y-shiftx,a,imaging.rRect(8,14,0x111111)))
    return toren
