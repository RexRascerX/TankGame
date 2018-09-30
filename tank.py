# The thing you make when a tank apears
import tread, chassis, turrets
import imaging, eventHandler
import pygame

# User defined tanks
class tank:
  eve = eventHandler.eventOV() 
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
    if tank.eve.queue.count(pygame.K_UP) > 0:
      self.y -= 1
    if tank.eve.queue.count(pygame.K_DOWN) > 0:
      self.y += 1
    if tank.eve.queue.count(pygame.K_LEFT) > 0:
      self.x -= 1
    if tank.eve.queue.count(pygame.K_RIGHT) > 0:
      self.x += 1
    #self.a += 1
    #self.x += 1

#Shows stuff.
  def render(self):
    length = self.chassis.length
    width = self.chassis.width + self.locomotion.width * 2
    toren = []
    toren.append(imaging.rImage(self.x,self.y,self.a,imaging.rRect(length,width,0x000000)))
    for x in range(self.locomotion.numRen()): 
      toren[0].addrect((x%2)*(self.chassis.length-self.locomotion.length),(x//2)*(self.chassis.width+self.locomotion.width),0,self.locomotion.render())
    toren[0].addrect(0,self.locomotion.width,0,self.chassis.render())
    for x in self.secondaries:
      toren.append(x.render(self.x,self.y,self.secondaryAs[x]))
    for x in self.primaries:
      toren.append(x.render(self.x,self.y,self.primaryAs[x]))
    return toren

