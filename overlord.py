print("Gotta have that Cactus Swag")
import sys,pygame
pygame.init()

scr=pygame.display.set_mode((640,480))
bg=pygame.Surface(scr.get_size())
bg.fill((127,0,0))
bg=bg.convert()
scr.blit(bg,(0,0))
clk = pygame.time.Clock()
mainloop=True
pygame.display.set_caption("Zoned For War")

while mainloop:
 milliseconds = clk.tick()
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