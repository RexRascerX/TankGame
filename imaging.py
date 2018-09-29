
#Images that can be tossed into the render queue any time
class rImage:
 def __init__(self,x,y,a,rect):
  this.x=x#x coord
  this.y=y#y coord
  this.a=a#angle
  this.rect=rect#sprite
 def render(self,frame):
  this.rect.blit(this,frame,(this.x,this.y),a)

#Polygons in need of rendering
class rRect:
 def __init__(self,w,h,c):
  this.serf=Surface((h,w))
  this.serf.fill(c)
  this.serf.fill(0x000000,Rect(2,2,w-4,h-4))
  
 def blit(self,target,pos,angle):
  赤=copy.copy(serf)
  rotate(赤,angle)
  赤.blit(target,pos)
