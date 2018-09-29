#Initialization stuff
import sys,pygame,imaging,copy
import tank,tread,chassis,turrets
pygame.init()
scr=pygame.display.set_mode((640,480))
bg=pygame.Surface(scr.get_size())
bg.fill((127,0,0))
bg=bg.convert()
scr.blit(bg,(0,0))
clk = pygame.time.Clock()
mainloop=True
pygame.display.set_caption("Zoned For War")
playtime=0

#Game status stuff
gmodes=["title","lselect","match","customize"]
gmode=gmodes[0]

#Graphics fun stuff
rq=[]

#Note that the default facing angle is to the right-hand edge of the screen (-->) and that rotations are counterclockwise when positive and clockwise when negative

def ttick():
 print("title")
 
def ltick():
 print("level select")
 
#Battle mode stuff
eq=[]
 
def btick():
 for エ in eq:
   trq=エ.render()
   for t in trq:
    rq.append(t)
 print("in battle")
 
def ctick():
 print("customization")

# The structural loops
def tick():
 if(gmode==gmodes[0]):
  ttick()
 if(gmode==gmodes[1]):
  ltick()
 if(gmode==gmodes[2]):
  btick()
 if(gmode==gmodes[3]):
  ctick()
 print("ticking")
 
def render():
 bg.fill((127,0,0))
 for ロ in rq:
  ロ.render(bg)
 bg=bg.convert()
 scr.blit(bg,(0,0))
 pygame.display.flip()
 print("rendered")

#Adding Tank to test
Tester = tank.tank(tread.wheels(0), chassis.lightChassis(0))
eq.append(Tester.render())

while mainloop:
 milliseconds = clk.tick()
 playtime+=milliseconds/1000.0
 #check events
 for event in pygame.event.get():
  # User presses QUIT-button.
  if event.type == pygame.QUIT:
   mainloop = False 
  elif event.type == pygame.KEYDOWN:
   # User presses ESCAPE-Key
   if event.key == pygame.K_ESCAPE:
    gmode=gmodes[0]
 # Print framerate and playtime in titlebar.
 render()
 #Update Pygame display.
