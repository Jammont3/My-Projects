import pygame
import time
import numpy
from helpers import update

pygame.init()

global board
global neighbors

BLACK = (0, 0, 0)
GREY = (128, 128, 128)
YELLOW = (255, 255, 0)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

BOARD_WIDTH = 5
BOARD_HEIGHT = 5

TILE_SIZE = SCREEN_WIDTH // BOARD_WIDTH

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

board = [[numpy.random.random_integers(0, 1) for i in SCREEN_HEIGHT] for j in SCREEN_WIDTH]

run = True
while run:

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
  
  screen.fill(GREY)
  board = update(board)

  time.sleep(2)
pygame.quit()