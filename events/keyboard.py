import pygame, sys

class eventOV:
  queue = []
  exit = False
  def __init__(self):
    None
  def __str__(self):
    return "Why? Just why have you done this? Are you happy now?"
  def check(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        eventOV.exit = True
      if event.type == pygame.KEYDOWN:
        eventOV.queue.append(event.key)
      if event.type == pygame.KEYUP:
        eventOV.queue.remove(event.key)
   # print(eventOV.queue)
  def noKeys(self):
    return len(eventOV.queue) == 0
  def end(self):
    return exit


