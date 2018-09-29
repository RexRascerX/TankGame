#Initialization stuff
import sys,pygame,mouse
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

#Images that can be tossed into the render queue any time
class rImage:
 def __init__(self,x,y,a,spr):
  this.x=x#x coord
  this.y=y#y coord
  this.a=a#angle
  this.spr=spr#sprite

#Polygons in need of rendering
class rRect:
 def __init__(self,w,h,c):
  serf=Surface((h,w))
  serf.fill(0x00FF00)
  serf.fill(0x000000,Rect(2,2,w-4,h-4))

def ttick():
 print("Currently in the title menu")
 
def ltick():
 print("level select")

# The structural loops
def tick():
 if(gmode==gmodes[0]):
  ttick()
 if(gmode==gmodes[1]):
  ltick()
 print("ticking")
 
def render():
 print("rendering")

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
    mainloop = False
 # Print framerate and playtime in titlebar.
 #Update Pygame display.
 pygame.display.flip()