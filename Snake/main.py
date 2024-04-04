import pygame
import random
from display_helpers import *
from game_helpers import *
from computer import *

DIRECTION = enumerate(['UP', 'DOWN', 'LEFT', 'RIGHT'])

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

TILE_SIZE = 20

GRID_WIDTH = SCREEN_WIDTH // TILE_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // TILE_SIZE

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

length = 3
direction = 'LEFT'
tail, apple_pos = gen(GRID_WIDTH, GRID_HEIGHT)

update_screen(screen, tail, apple_pos, TILE_SIZE)

run = True
playing = False

while run:

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
        playing = not playing
      if event.key == pygame.K_UP:
        if direction != 'DOWN': direction = 'UP'
        if not playing: playing = True
      if event.key == pygame.K_DOWN:
        if direction != 'UP': direction = 'DOWN'
        if not playing: playing = True
      if event.key == pygame.K_LEFT:
        if direction != 'RIGHT': direction = 'LEFT'
        if not playing: playing = True
      if event.key == pygame.K_RIGHT:
        if direction != 'LEFT': direction = 'RIGHT'
        if not playing: playing = True
  
  if (playing): 
    direction = get_move_algo1(tail, apple_pos, direction)
    tail = move(tail, direction, length)
    pos = tail[-1]
    if pos in tail[:-1] or (pos[0] < 0 or pos[1] < 0 or pos[0] > GRID_WIDTH - 1 or pos[1] > GRID_HEIGHT - 1):
      print("You Died")
      print("Score: " + str(length - 3))
      direction = 'LEFT'
      length = 3
      tail, apple_pos = gen(GRID_WIDTH, GRID_HEIGHT)
      playing = False
    if pos == apple_pos:
      length += 1
      while True:
        apple_pos = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
        if apple_pos not in tail: break
    update_screen(screen, tail, apple_pos, TILE_SIZE)
  pygame.time.delay(10)