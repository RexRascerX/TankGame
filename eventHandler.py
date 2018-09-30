import pygame, sys

class eventOV:
    queue = []
    exit = False
  def __init__(self):
    pg = pygame
  def __str__(self):
    return "Why? Just why have you done this? Are you happy now?"
  def check(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        exit = True
      if event.type == pygame.KEYDOWN:
        queue.append(event.key)
      if event.type == pygame.KEYUP:
        queue.remove(event.key)
    print(queue)
  def noKeys():
    return len(queue) == 0
  def end():
    return exit


