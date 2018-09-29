# The center of the Tank

# This is the inheritance version. Please do not use
# Please make versions below
def chassis:
  def __init__(self, primary, secondary, armorBonus, energyCapacity, chargeRate):
    self.primary = primary
    self.secondary = secondary
    self.energyCapacity = energyCapacity
    self.chargeRate = chargeRate
  def __str__(self):
    return "Chassis"

# Please make types below or use them.
def lightChassis(chassis):
  def __init__(self, level):
    super().__init__((level//3),(2+level)//2, level, 7*(level+1), level)
  def __str__(self):
    return "Light Chassis"

# Make mediumChassis
# primary 1 for level 0, increase by 1 every 5 levels
# secondary 2 for level 0, increase by one every 3 levels
# armorBonus 2 per level, 4 at level 0.
# energyCapacity 10 per level, 10 at level 0.
# chargeRate level plus 1.

# Make heavyChassis
# primary 1 for level 0, increase by 1 every 3 levels
# secondary 2 for level 0, increase by one every 2 levels
# armorBonus 3 per level, 5 at level 0.
# energyCapacity 13 per level, 13 at level 0.
# chargeRate level plus 2.
