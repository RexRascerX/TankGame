# The thing you make when a tank apears
import tread, chassis, turrets
import imaging

# User defined tanks
class tank:
  def __init__(self,locomotion, chassis, xya):
    self.locomotion = locomotion
    self.chassis = chassis
    self.powerTotal = -1
    self.powerLevel = 0
    self.primaries = []
    self.secondaries = []
    self.x = xya[0]
    self.y = xya[1]
    self.a = xya[2]
    self.primaryAs = {}
    self.secondaryAs = {}
  def __str__(self):
    return "Tank"
  def addPrimary(self, turret):
    if (self.primaries.count() < self.chassis.primary):
      self.primaries.append(turret)
      self.primaryAs.update(turret,self.a)
    else:
      print("Denied Primary " + turret)
  def addSecondary(self, turret):
    if (self.secondaries.count() < self.chassis.secondary):
      self.secondaries.append(turret)
      self.secondaryAs.update(turret,self.a)
    else:
      print("Denied Secondary " + turret)
  def getPowerTotal():
    self.powerTotal = chassis.energyCapacity
    for x in self.primaries:
      if x.type() == 1:
        if x.energy() != -1:
          self.powerTotal += x.energy()
    for x in self.secondaries:
      if x.type() == 1:
        if x.energy() != -1:
          self.powerTotal += x.energy()
    self.powerLevel = self.powerTotal
  def getPowerLevel(self):
    if self.powerTotal == -1:
      self.getPowerTotal()
    return self.powerTotal
  def render(self):
    toren = []
    for x in locomotion.render(self.x,self.y,self.a,chassis.width()/2,chassis.hight()/2):
      toren.append(x)
    toren.append(chassis.render(self.x,self.y,self.a)
    for x in self.secondaries:
      toren.append(x.render(self.x,self.y,self.secondaryAs[x]))
    for x in self.primaries:
      toren.append(x.render(self.x,self.y,self.primaryAs[x]))
    return toren

