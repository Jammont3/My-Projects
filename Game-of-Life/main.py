import pygame
import random
from helpers import update

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

f = open("grid.txt", "r")
board = set()
y = 0
x = 0
for line in f.readlines():
  x = 0
  for val in line.split(" "):
    if (val == "1"): 
      board.add((x, y))
    x += 1
  y += 1

BOARD_WIDTH = x
BOARD_HEIGHT = y

TILE_SIZE = SCREEN_WIDTH // BOARD_WIDTH

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill(BLACK)

pygame.display.flip()

run = True
playing = False

while run:
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
        print(board)
      if event.key == pygame.K_c:
        board = set()
      if event.key == pygame.K_r:
        board = set()
        for x in range(BOARD_WIDTH):
          for y in range(BOARD_HEIGHT):
            if (random.randint(0, 100) > 40):
              board.add((x, y))

  if playing:
    board = update(board)

  screen.fill(BLACK)
  for pos in board:
    x = pos[0]
    y = pos[1]
    pygame.draw.rect(screen, WHITE, pygame.Rect(TILE_SIZE * x, TILE_SIZE * y, TILE_SIZE, TILE_SIZE))


  pygame.display.flip()
  pygame.time.delay(100)

pygame.quit()