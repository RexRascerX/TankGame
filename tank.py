# The thing you make when a tank apears
import tread.py, chassis.py

# User defined tanks
def tank:
  def __init__(self,locomotion, chassis):
    self.locomotion = locomotion
    self.chassis = chassis
  def __str__(self):
    return "Tank"
  
