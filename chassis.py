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

