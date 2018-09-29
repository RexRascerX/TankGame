# The thing you make when a tank apears
import tread, chassis, turrets
import imaging

# User defined tanks
class tank:
  def __init__(self,locomotion, chassis):
    self.locomotion = locomotion
    self.chassis = chassis
    self.powerTotal = -1
    self.powerLevel = 0
    self.primaries = []
    self.secondaries = []
  def __str__(self):
    return "Tank"
  def addPrimary(turret):
    if (self.primaries.count() < self.chassis.primary):
      self.primaries.append(turret)
    else:
      print("Denied Primary " + turret)
  def addSecondary(turret):
    if (self.secondaries.count() < self.chassis.secondary):
      self.secondaries.append(turret)
    else:
      print("Denied Secondary " + turret)
  def getPowerTotal():
    powerTotal = chassis.energyCapacity
    for x in primaries:
      if x.type() == 1:
        if x.energy() != -1:
          powerTotal += x.energy()
    for x in secondaries:
      if x.type() == 1:
        if x.energy() != -1:
          powerTotal += x.energy()
    powerLevel = powerTotal
  def getPowerLevel():
    if powerTotal == -1:
      getPowerTotal()
    return powerTotal
  def render(self):
    return imaging.rImage(10,10,0,imaging.rRect(5,12,0xFFFFFF))
