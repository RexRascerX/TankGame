print("Gotta have that Cactus Swag")
import sys,pygame,mouse
pygame.init()

#Define some overarching code

scr=pygame.display.set_mode((640,480))
bg=pygame.Surface(scr.get_size())
bg.fill((127,0,0))
bg=bg.convert()
scr.blit(bg,(0,0))
clk = pygame.time.Clock()
mainloop=True
pygame.display.set_caption("Zoned For War")
playtime=0

while mainloop:
 milliseconds = clk.tick()
 playtime+=milliseconds/1000.0
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