# The center of the Tank

# This is the inheritance version. Please do not use
# Please make versions below
class chassis:
  def __init__(self, primary, secondary, armorBonus, energyCapacity, chargeRate):
    self.primary = primary
    self.secondary = secondary
    self.armorBonus = armorBonus
    self.energyCapacity = energyCapacity
    self.chargeRate = chargeRate
  def __str__(self):
    return "Chassis"
  def render(self, x,y,a):
    pass

# Please make types below or use them.
class lightChassis(chassis):
  def __init__(self, level):
    super().__init__((level//3),(2+level)//2, level, 7*(level+1), level)
  def __str__(self):
    return "Light Chassis"
  def length(self):
    return 30
  def render(self, x,y,a):
    return imaging.rImage(x,y,a,imaging.rRect(24,30,0xFFFFFF))

class mediumChassis(chassis):
  def __init__(self, level):
    super().__init__((level+5)//5,(level+6)//3,(2*level)+4,(10*level)+10, level+1)
  def __str__(self):
    return "Medium Chassis"
  def length(self):
    return 38
  def render(self, x,y,a):
    return imaging.rImage(x,y,a,imaging.rRect(28,38,0xFFFFFF))

class heavyChassis(chassis):
  def __init__(self, level):
    super().__init__((level+3)//3,(level+4)//2,(3*level)+5,(13*level)+13,level+2)
  def __str__(self):
    return "Heavy Chassis"
  def length(self):
    return 46
  def render(self, x,y,a):
    return imaging.rImage(x,y,a,imaging.rRect(32,46,0xFFFFFF))

