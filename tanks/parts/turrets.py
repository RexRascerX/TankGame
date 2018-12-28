# This file is for tank bits and bobs
from draw import imaging
import pygame

class turret:
    def __init__(self, sightLength, turningSpeed, energyConsumption, armorBonus):
        self.sightLength = sightLength
        self.turningSpeed = turningSpeed
        self.energyConsumption = energyConsumption
        self.armorBonus = armorBonus
    def __str__(self):
        return "Turret"
    def action(self):
        -self.energyConsumption
    def type(self):
        return 0;
    def primaryRender(self):
      pass

class passiveTurret(turret):
    def __init__(self, sightLength, turningSpeed, energyConsumption, armorBonus):
        super().__init__(sightLength, turningSpeed, energyConsumption, armorBonus)
    def __str__(self):
        return "Passive Turret"
    def type(self):
        return 1;
    def energy(self):
      pass
    def matter(self):
      pass
    def primaryRender(self):
      pass

class aggressiveTurret(turret):
    def __init__(self, sightLength, turningSpeed, energyConsumption, armorBonus):
        super().__init__(sightLength, turningSpeed, energyConsumption, armorBonus)
    def __str__(self):
        return "Aggressive Turret"
    def type(self):
        return -1;
    def primaryRender(self):
      pass

class matter(aggressiveTurret):
    def __init__(self, sightLength, turningSpeed, energyConsumption, armorBonus, matterStorage):
        self.matterStorage = matterStorage
        super().__init__(sightLength, turningSpeed, energyConsumption, armorBonus)
    def __str__(self):
        return "Matter based turret"
    def primaryRender(self):
      pass
        
class energy(aggressiveTurret):
    def __init__(self, sightLength, turningSpeed, energyConsumption, armorBonus):
        super().__init__(sightLength, turningSpeed, energyConsumption, armorBonus)
    def __str__(self):
        return "Energy based turret"
    def primaryRender(self):
      pass

class GaussRifle(matter):
    def __init__(self, level):
        self.length = 19
        self.width = 8
        super().__init__(10+level, 2, 1+(level/3), 3, 3)
    def __str__(self):
        return "Gauss Rifle"
    def primaryRender(self, x, y, a):
        return imaging.rImage(x,y,a,imaging.rRect(self.length,self.width,0x10ff10))
    def secondaryRender(self):
        return imaging.rRect(self.length,self.width,0xFFFFFF)
class Type67(matter):
    def __init__(self, level):
        self.length = 14
        self.width = 8
        super().__init__(3+(level/4), 8+(level/2), 0.1+(level/5), 7, 1)
    def __str__(self):
        return "Type 67"
    def primaryRender(self, x, y, a):
        return imaging.rImage(x,y,a,imaging.rRect(self.length,self.width,0x10ff10))
    def secondaryRender(self):
        return imaging.rRect(self.length,self.width,0xFFFFFF)
        
class BigBertha(matter):
    def __init__(self, level):
        self.length = 16
        self.width = 8
        super().__init__(6+level, 3+(level/2), 3+(level/2), 5, 5)
    def __str__(self):
        return "Big Bertha"
    def primaryRender(self, x, y, a):
        return imaging.rImage(x,y,a,imaging.rRect(self.length,self.width,0x10ff10))
    def secondaryRender(self):
        return imaging.rRect(self.length,self.width,0xFFFFFF)
class ElectronNeedler(energy):
    def __init__(self, level):
        self.length = 19
        self.width = 8
        super().__init__(10+level, 2, 5+(level/2), 3)
    def __str__(self):
        return "Electron Needler"
    def primaryRender(self, x, y, a):
        return imaging.rImage(x,y,a,imaging.rRect(self.length, self.width, 0xff00ff))
    def secondaryRender(self):
        return imaging.rRect(self.length,self.width,0xFFFFFF)
class ProtonBlaster(energy):
    def __init__(self, level):
        self.length = 14
        self.width = 8
        super().__init__(3+(level/4), 8+(level/2), 0.4+(level/3), 7)
    def __str__(self):
        return "Proton Blaster"
    def primaryRender(self, x, y, a):
        return imaging.rImage(x,y,a,imaging.rRect(self.length, self.width,0xff00ff))
    def secondaryRender(self):
        return imaging.rRect(self.length,self.width,0xFFFFFF)
class NeutronNeuterer(energy):
    def __init__(self, level):
        self.length = 16
        self.width = 8
        super().__init__(6+level, 3+(level/2), 5+level, 5)
    def __str__(self):
        return "Neutron Neuterer"
    def primaryRender(self, x, y, a):
        return imaging.rImage(x,y,a,imaging.rRect(self.length,self.width,0xff00ff))
    def render(self):
        return imaging.rRect(self.length,self.width,0xFFFFFF)
