import pygame,copy

#Images that can be tossed into the render queue any time
class rImage:
 def __init__(self,x,y,a,rect):
  print("rImage.draw()")
  self.x=x#x coord
  self.y=y#y coord
  self.a=a#angle
  self.rect=rect#sprite
 def render(self,frame):
  print("rImage.draw()")
  self.rect.draw(frame,self.x,self.y,self.a)

#Polygons in need of rendering
class rRect:
 def __init__(self,w,h,c):
  print("rRect.init()")
  self.serf=pygame.Surface((h,w))
  self.serf.fill(0xFFFFFF)
  self.serf.fill(0x000000,pygame.Rect(2,2,w-4,h-4))
  
 def draw(self,target,x,y,angle):
  print("rRect.draw()")
  赤=copy.copy(self.serf)
  pygame.transform.rotate(赤,angle)
  target.blit(赤,(x,y))