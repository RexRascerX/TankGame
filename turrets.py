def turret:
    def __init__(self, sightLength, turningSpeed, energyConsumption, armorBonus):
        self.sightLength = sightLength
        self.turningSpeed = turningSpeed
        self.energyConsumption = energyConsumption
        self.armorBonus = armorBonus
    def __str__(self):
        return "Turret"
    def action():
        pass
    def type():
        return 0;

def passiveTurret(turret):
    def __init__(self, sightLength, turningSpeed, energyConsumption, armorBonus):
        super().__init__(sightLength, turningSpeed, energyConsumption, armorBonus)
    def __str__(self):
        return "Passive Turret"
    def action():
        pass
    def type():
        return 1;

def aggressiveTurret(turret):
    def __init__(self, sightLength, turningSpeed, energyConsumption, armorBonus):
        super().__init__(sightLength, turningSpeed, energyConsumption, armorBonus)
    def __str__(self):
        return "Aggressive Turret"
    def action():
        pass
    def type():
        return -1;

def matter(aggressiveTurret):
    def __init__(self, sightLength, turningSpeed, energyConsumption, armorBonus):
        super().__init(sightLength, turningSpeed, energyConsumption, armorBonus)
    def __str__(self):
        return "Matter based turret"
    def action():
        pass

def energy(aggressiveTurret):
    def __init__(self, sightLength, turningSpeed, energyConsumption, armorBonus):
        super().__init(sightLength, turningSpeed, energyConsumption, armorBonus)
    def __str__(self):
        return "Energy based turret"
    def action():
        pass

def GaussRifle(matter):
    def __init__(self, level):
        super().__init(10+level, 2, 1+(level/3), 3)
    def __str__(self):
        return "Gauss Rifle"

def Type67(matter):
    def __init__(self, level):
        super().__init(3+(level/4), 8+(level/2), 0.1+(level/5), 7)
    def __str__(self):
        return "Type 67"

def BigBertha(matter):
    def __init__(self, level):
        super().__init(6+level, 3+(level/2), 3+(level/2), 5)
    def __str__(self):
        return "Big Bertha"

def ElectronNeedler(energy):
    def __init__(self, level):
        super().__init(10+level, 2, 5+(level/2), 3)
    def __str__(self):
        return "Electron Needler"

