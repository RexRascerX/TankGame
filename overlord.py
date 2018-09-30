#This is Jonathan's code almost exclusively. Any and all insanity contained within is likely his responsibility.

#Initialization stuff
import sys,pygame,imaging,copy
import tank,tread,chassis,turrets
import eventHandler

pygame.init()
scr=pygame.display.set_mode((640,480))
clk = pygame.time.Clock()
mainloop=True
pygame.display.set_caption("Zoned For War")
playtime=0

#Game status stuff
gmodes=["title","lselect","match","customize"]
gmode=0

#Graphics fun stuff
rq=[]

#Note that the default facing angle is to the right-hand edge of the screen (-->) and that rotations are counterclockwise when positive and clockwise when negative

def ttick():
    return None;
def ltick():
   return None; 
#Battle mode stuff
eq=[]
 
def btick():
 for エ in eq:
   エ.tick(1)
   trq=エ.render()
   for t in trq:
    rq.append(t)
 
def ctick():
 print("customization")

gticks=[ttick(),ltick(),btick(),ctick()]

# The structural loops
def tick():
 gticks[gmode]
 
def trender():
 bg=pygame.Surface(scr.get_size())
 bg.fill(0x0)
 
 bg=bg.convert()
 scr.blit(bg,(0,0))
 pygame.display.flip()
 
def brender(scr):
 bg=pygame.Surface(scr.get_size())
 bg.fill(0x0)
 for ロ in rq:
  ロ.render(bg)
 bg=bg.convert()
 scr.blit(bg,(0,0))
 pygame.display.flip()
 rq=[]
 
def render(scr):
 if(gmode==gmodes[0]):
  ttick()
 if(gmode==gmodes[1]):
  ltick()
 if(gmode==gmodes[2]):
  brender()
 if(gmode==gmodes[3]):
  ctick()

#Adding Tank to test
Tester = tank.tank(tread.wheels(0), chassis.lightChassis(0),(20,20,20))
rq.append(Tester.render())

eveHan = eventHandler.eventOV()

while mainloop:
 eveHan.check()
 tick()
 render(scr)
 #Update Pygame display.
