from draw import imaging
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
  def length(self):
    pass
  def width(self):
    pass
  def render(self):
    pass

# Please make types below or use them.
class lightChassis(chassis):
  def __init__(self, level):
    super().__init__((level//3),(2+level)//2, level, 7*(level+1), level)
    self.length = 30
    self.width = 24
  def __str__(self):
    return "Light Chassis"
  def length(self):
    return self.length
  def width(self):
    return self.width
  def render(self):
    return imaging.rRect(self.length,self.width,0xFFFFFF)

class mediumChassis(chassis):
  def __init__(self, level):
    super().__init__((level+5)//5,(level+6)//3,(2*level)+4,(10*level)+10, level+1)
    self.length = 38
    self.width = 28
  def __str__(self):
    return "Medium Chassis"
  def length(self):
    return self.length
  def width(self):
    return self.width
  def render(self):
    return imaging.rRect(self.length,self.width,0xFFFFFF)

class heavyChassis(chassis):
  def __init__(self, level):
    super().__init__((level+3)//3,(level+4)//2,(3*level)+5,(13*level)+13,level+2)
    self.length = 38
    self.width = 28
  def __str__(self):
    return "Heavy Chassis"
  def length(self):
    return self.length
  def width(self):
    return self.width
  def render(self):
    return imaging.rRect(self.length,self.width,0xFFFFFF)

