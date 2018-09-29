#Initialization stuff
import sys,pygame,imaging.py,copy
import tank.py
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
 print("rendering")

#Adding Tank to test
Tester = tank(wheels(0), lightChassis(0))

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
 #Update Pygame display.
 pygame.display.flip()
