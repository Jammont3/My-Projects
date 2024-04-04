import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

def update_screen(screen, tail, apple_pos, TILE_SIZE):
  screen.fill(BLACK)
  pygame.draw.rect(screen, RED, pygame.Rect(TILE_SIZE * apple_pos[0], TILE_SIZE * apple_pos[1], TILE_SIZE, TILE_SIZE))
  for pos in tail:
    pygame.draw.rect(screen, YELLOW, pygame.Rect(TILE_SIZE * pos[0], TILE_SIZE * pos[1], TILE_SIZE, TILE_SIZE))
  pygame.display.flip()