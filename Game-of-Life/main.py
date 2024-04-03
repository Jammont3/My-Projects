import pygame
import random
from helpers import *

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

TILE_SIZE = 10

BOARD_WIDTH = SCREEN_WIDTH // TILE_SIZE
BOARD_HEIGHT = SCREEN_HEIGHT // TILE_SIZE

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill(BLACK)

pygame.display.flip()

board = set()

run = True
playing = False

tick_speed = 90

while run:
  board = move_board(board)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
    
    if event.type == pygame.MOUSEBUTTONDOWN:
      x, y = pygame.mouse.get_pos()
      row = x // TILE_SIZE
      col = y // TILE_SIZE
      if (row, col) in board:
        board.remove((row, col))
      else:
        board.add((row, col))

    if  event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
        playing = not playing
      if event.key == pygame.K_RIGHT:
        board = update(board)
      if event.key == pygame.K_UP:
        #tick_speed += 10
        TILE_SIZE += 1
        BOARD_WIDTH = SCREEN_WIDTH // TILE_SIZE
        BOARD_HEIGHT = SCREEN_HEIGHT // TILE_SIZE
      if event.key == pygame.K_DOWN:
        #tick_speed -= 10
        TILE_SIZE -= 1
        BOARD_WIDTH = SCREEN_WIDTH // TILE_SIZE
        BOARD_HEIGHT = SCREEN_HEIGHT // TILE_SIZE
      if event.key == pygame.K_c:
        board = set()
      if event.key == pygame.K_r:
        board = set()
        for x in range(BOARD_WIDTH):
          for y in range(BOARD_HEIGHT):
            if (random.randint(0, 100) > 50):
              board.add((x, y))

  if playing:
    board = update(board)

  screen.fill(BLACK)
  for pos in board:
    x = pos[0]
    y = pos[1]
    pygame.draw.rect(screen, WHITE, pygame.Rect(TILE_SIZE * x, TILE_SIZE * y, TILE_SIZE, TILE_SIZE))


  pygame.display.flip()
  pygame.time.delay(tick_speed)

pygame.quit()