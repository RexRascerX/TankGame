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
#Needs to be run if you want weapons
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

#This calculates basic stats
  def getPowerTotal(self):
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

  def tick(self, num):


#Shows stuff.
  def render(self):
    toren = []
    for x in self.locomotion.render(self.x,self.y,self.a,self.chassis.width/2,self.chassis.length/2):
      toren.append(x)
    toren.append(self.chassis.render(self.x,self.y,self.a))
    for x in self.secondaries:
      toren.append(x.render(self.x,self.y,self.secondaryAs[x]))
    for x in self.primaries:
      toren.append(x.render(self.x,self.y,self.primaryAs[x]))
    return toren

