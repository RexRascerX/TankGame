# The thing you make when a tank apears
import tread.py, chassis.py, turrets.py

# User defined tanks
def tank:
  def __init__(self,locomotion, chassis):
    self.locomotion = locomotion
    self.chassis = chassis
    self.primaries = []
    self.secondaries = []
  def __str__(self):
    return "Tank"
  def addPrimary(turret):
    if (self.primaries.count() < self.chassis.primary):
      self.primaries.append(turret)
    else
      print("Denied Primary " + turret)
  def addSecondary(turret):
    if (self.secondaries.count() < self.chassis.secondary):
      self.secondaries.append(turret)
    else
      print("Denied Secondary " + turret)

