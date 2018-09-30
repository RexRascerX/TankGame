import pygame,copy

#Images that can be tossed into the render queue any time
class rImage:
 def __init__(self,x,y,a,rect):
  self.x=x#x coord
  self.y=y#y coord
  self.a=a#angle
  self.serf=rect.serf#sprite
 def addrect(self,x,y,a,rect):
  赤=copy.copy(rect.serf)
  pygame.transform.rotate(赤,a)
  self.serf.blit(赤,(x,y))
 def addsurf(self,x,y,a,surf):
  赤=copy.copy(surf)
  pygame.transform.rotate(赤,a)
  self.serf.blit(赤,(x,y))
 def render(self,frame):
  赤=copy.copy(self.serf)
  pygame.transform.rotate(赤,self.a)
  frame.blit(赤,(self.x,self.y))

#Polygons in need of rendering
class rRect:
 def __init__(self,w,h,c):
  self.serf=pygame.Surface((w,h))
  self.serf.fill(c)
  self.serf.fill(0x0,pygame.Rect(2,2,w-4,h-4))
  
 def draw(self,target,x,y,angle):
  赤=copy.copy(self.serf)
  pygame.transform.rotate(赤,angle)
  target.blit(赤,(x,y))