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
  def render(self, x, y, a, width, length):
    x1 = x + numpy.cos(a) * x  
    y1 = y - numpy.sin(a) * y
    x2 = x + numpy.sin(a) * x
    y2 = y + numpy.cos(a) * y
    toren = [imaging.rImage(x1,y1,a,imaging.rRect(self.width,self.length,0xBBA1BB))]
    toren.append(imaging.rImage(x2,y1,a,imaging.rRect(self.width,self.length,0xA1BBBB)))
    toren.append(imaging.rImage(x1,y2,a,imaging.rRect(self.width,self.length,0xBBBBA1)))
    toren.append(imaging.rImage(x2,y2,a,imaging.rRect(self.width,self.length,0xA1A1A1)))
    return toren

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
