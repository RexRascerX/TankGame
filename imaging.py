import pygame

#Images that can be tossed into the render queue any time
class rImage:
 def __init__(self,x,y,a,rect):
  self.x=x#x coord
  self.y=y#y coord
  self.a=a#angle
  self.rect=rect#sprite
 def render(self,frame):
  self.rect.blit(this,frame,(this.x,this.y),a)

#Polygons in need of rendering
class rRect:
 def __init__(self,w,h,c):
  self.serf=pygame.Surface((h,w))
  self.serf.fill(0xFFFFFF)
  self.serf.fill(0x000000,pygame.Rect(2,2,w-4,h-4))
  
 def blit(self,target,pos,angle):
  赤=copy.copy(serf)
  rotate(赤,angle)
  赤.blit(target,pos)
