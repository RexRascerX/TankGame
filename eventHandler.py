import pygame, sys

class eventOV:
  def __init__(self, pygame):
    self.pg = pygame
    self.queue = []
    self.exit = False
  def __str__(self):
    return "Why? Just why have you done this?"
  def check():
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        exit = True
      if event.type == pygame.KEYDOWN:
        queue.append(event.key)
  def next():
    if queue.count() > 0:
      temp = queue[0]
      queue.pop(0)
      return temp
    else
      return -1
  def empty():
    return queue.count() == 0
  def end():
    return exit

