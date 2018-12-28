#This is Jonathan's code almost exclusively. Any and all insanity contained within is likely his responsibility.

#Initialization stuff
import sys,pygame,copy,numpy
from tanks import tank
from tanks.parts import chassis
from tanks.parts import tread
from tanks.parts import turrets
from draw import imaging
from events import keyboard as eventHandler

pygame.init()
#pygame.mixer.music.load("Doomsday.wav")
#pygame.mixer.music.play(-1,0)

scr=pygame.display.set_mode((640,480))
clk = pygame.time.Clock()
mainloop=True
pygame.display.set_caption("Zoned For War")
playtime=0

#Game status stuff
gmodes=["title","lselect","match","customize"]
gmode=2

#Graphics fun stuff
rq=[]
FPS=60

#Note that the default facing angle is to the right-hand edge of the screen (-->) and that rotations are counterclockwise when positive and clockwise when negative

def ttick(eq):
 return None;
def ltick(eq):
 return None;
#Battle mode stuff
eq=[]

def btick(eq):
 for エ in eq:
   エ.tick(1)
   if(エ!=Chester):
    if((eq[0].x-エ.x)*(eq[0].x-エ.x)+(eq[0].y-エ.y)*(eq[0].y-エ.y)<10000):
     trq=エ.render()
     for t in trq:
      rq.append(t)
   else:
    trq=エ.render()
    for t in trq:
     rq.append(t)

def ctick(eq):
 print("customization")

# The structural loops
def tick(gmode,eq):
 if(gmode==0):
  ttick(eq)
 elif(gmode==2):
  btick(eq)

def trender(scr,rq):
 bg=pygame.Surface(scr.get_size())
 bg.fill(0x00FF00)
 bg=bg.convert()
 scr.blit(bg,(0,0))
 pygame.display.flip()

def brender(scr,rq):
 bg=pygame.Surface(scr.get_size())
 bg.fill(0x0)
 for ロ in rq:
  ロ.render(bg)
 bg=bg.convert()
 scr.blit(bg,(0,0))
 pygame.display.flip()
 rq.clear()

def render(gmode,scr,rq):
 if(gmode==0):
  trender(scr,rq)
 elif(gmode==2):
  brender(scr,rq)

#Adding Tank to test
Chester = tank.tank(tread.wheels(0), chassis.mediumChassis(0),(20,20,0),True)
Chester.addPrimary(turrets.BigBertha(0))
eq.append(Chester)
Howard = tank.tank(tread.wheels(0), chassis.mediumChassis(0),(599,29,0),False)
eq.append(Howard)
William = tank.tank(tread.wheels(0), chassis.mediumChassis(0),(371,241,0),False)
eq.append(William)
George = tank.tank(tread.wheels(0), chassis.mediumChassis(0),(59,380,0),False)
eq.append(George)

eveHan = eventHandler.eventOV()

while mainloop:
 milliseconds = clk.tick(FPS)
 eveHan.check()
 mainloop = not eveHan.exit
 tick(gmode,eq)
 render(gmode,scr,rq)
 #Update Pygame display.
# The below line is to be IDLE friendly
pygame.quit()
