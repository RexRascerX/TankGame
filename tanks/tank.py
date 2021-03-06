# The thing you make when a tank apears
from tanks.parts import tread, chassis, turrets
from draw import imaging 
import events.keyboard as eventHandler
import pygame, numpy

# User defined tanks
class tank:
  eve = eventHandler.eventOV() 
  def __init__(self,locomotion, chassis, xya, pc):
    self.pc=pc
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
    self.dead=False
  def __str__(self):
    return "Tank"
#Needs to be run if you want weapons
  def addPrimary(self, turret):
    if len(self.primaries) < self.chassis.primary:
      self.primaries.append(turret)
      self.primaryAs.update({turret:self.a})
    else:
      print("Denied Primary " + str(turret))
  def addSecondary(self, turret):
    if len(self.secondaries) < self.chassis.secondary:
      self.secondaries.append(turret)
      self.secondaryAs.update(turret,self.a)
    else:
      print("Denied Secondary " + str(turret))

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

  def tick(self, time):
   if self.pc:
    if tank.eve.queue.count(pygame.K_UP) > 0:
      self.y += 1 * numpy.sin(-self.a/180*numpy.pi)
      self.x += 1 * numpy.cos(-self.a/180*numpy.pi)
    if tank.eve.queue.count(pygame.K_DOWN) > 0:
      self.y -= 1 * numpy.sin(-self.a/180*numpy.pi)
      self.x -= 1 * numpy.cos(-self.a/180*numpy.pi)
    if tank.eve.queue.count(pygame.K_LEFT) > 0:
      self.a += self.locomotion.turnSpeed
      self.primaryAs[self.primaries[0]] += self.locomotion.turnSpeed
    if tank.eve.queue.count(pygame.K_RIGHT) > 0:
      self.a -= self.locomotion.turnSpeed
      self.primaryAs[self.primaries[0]] -= self.locomotion.turnSpeed
    if len(self.primaries) > 0:
        if tank.eve.queue.count(pygame.K_d) > 0:
            self.primaryAs[self.primaries[0]] -= self.primaries[0].turningSpeed
        if tank.eve.queue.count(pygame.K_a) > 0:
            self.primaryAs[self.primaries[0]] += self.primaries[0].turningSpeed

    #self.a += 1
    #self.x += 1

#Shows stuff.
  def render(self):
    if(self.dead):
     return []
    length = self.chassis.length
    width = self.chassis.width + self.locomotion.width * 2
    toren = []
    toren.append(imaging.rImage(self.x,self.y,self.a,imaging.rRect(length,width,0x000000)))
	
    for x in range(self.locomotion.numRen()): 
      toren[0].addrect((x%2)*(self.chassis.length-self.locomotion.length-4),(x//2)*(self.chassis.width+self.locomotion.width),0,self.locomotion.render())
    toren[0].addrect(0,self.locomotion.width,0,self.chassis.render())
    for x in self.secondaries:
      toren[0].addrect(length/2,width/2,0,x.secondaryRender())
    for x in self.primaries:
      toren.append(x.primaryRender(self.x+length/2,self.y+width/2,self.primaryAs[x]))
    return toren

