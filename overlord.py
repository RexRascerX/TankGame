#This is Jonathan's code almost exclusively. Any and all insanity contained within is likely his responsibility.

#Initialization stuff
import sys,pygame,imaging,copy
import tank,tread,chassis,turrets
import eventHandler

pygame.init()
pygame.mixer.music.load("Doomsday.wav")
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
Tester = tank.tank(tread.wheels(0), chassis.lightChassis(0),(20,20,0))
eq.append(Tester)

eveHan = eventHandler.eventOV()

while mainloop:
 eveHan.check()
 mainloop = not eveHan.exit
 tick(gmode,eq)
 render(gmode,scr,rq)
 #Update Pygame display.
