def turret:
    def __init__(self, sightLength, turningSpeed, energyConsumption, armorBonus):
        self.sightLength = sightLength
        self.turningSpeed = turningSpeed
        self.energyConsumption = energyConsumption
        self.armorBonus = armorBonus
    def __str__(self):
        return "Turret"

