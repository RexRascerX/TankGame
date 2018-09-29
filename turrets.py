# This file is for tank bits and bobs
import imaging, pygame

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
    def render(self):
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
    def render(self):
      pass

class aggressiveTurret(turret):
    def __init__(self, sightLength, turningSpeed, energyConsumption, armorBonus):
        super().__init__(sightLength, turningSpeed, energyConsumption, armorBonus)
    def __str__(self):
        return "Aggressive Turret"
    def type(self):
        return -1;
    def render(self):
      pass

class matter(aggressiveTurret):
    def __init__(self, sightLength, turningSpeed, energyConsumption, armorBonus, matterStorage):
        self.matterStorage = matterStorage
        super().__init__(sightLength, turningSpeed, energyConsumption, armorBonus)
    def __str__(self):
        return "Matter based turret"
    def render(self):
      pass
        
class energy(aggressiveTurret):
    def __init__(self, sightLength, turningSpeed, energyConsumption, armorBonus):
        super().__init__(sightLength, turningSpeed, energyConsumption, armorBonus)
    def __str__(self):
        return "Energy based turret"
    def render(self):
      pass

class GaussRifle(matter):
    def __init__(self, level):
        super().__init__(10+level, 2, 1+(level/3), 3, 3)
    def __str__(self):
        return "Gauss Rifle"
    def render(self):
      

class Type67(matter):
    def __init__(self, level):
        super().__init__(3+(level/4), 8+(level/2), 0.1+(level/5), 7, 1)
    def __str__(self):
        return "Type 67"
        
class BigBertha(matter):
    def __init__(self, level):
        super().__init__(6+level, 3+(level/2), 3+(level/2), 5, 5)
    def __str__(self):
        return "Big Bertha"
    
class ElectronNeedler(energy):
    def __init__(self, level):
        super().__init__(10+level, 2, 5+(level/2), 3)
    def __str__(self):
        return "Electron Needler"
    
class ProtonBlaster(energy):
    def __init__(self, level):
        super().__init__(3+(level/4), 8+(level/2), 0.4+(level/3), 7)
    def __str__(self):
        return "Proton Blaster"
    
class NeutronNeuterer(energy):
    def __init__(self, level):
        super().__init__(6+level, 3+(level/2), 5+level, 5)
    def __str__(self):
        return "Neutron Neuterer"
    
