global HEIGHT
global WIDTH
def init(SCREEN_WIDTH, SCREEN_HEIGHT, TILE_SIZE):
  HEIGHT = SCREEN_HEIGHT // TILE_SIZE
  WIDTH = SCREEN_WIDTH // TILE_SIZE

def get_move_algo1(tail, apple_pos, direction):
  pos = tail[-1]
  x_diff = apple_pos[0] - pos[0]
  y_diff = apple_pos[1] - pos[1]
  if (x_diff < 0 and direction != 'RIGHT' and (pos[0] - 1, pos[1]) not in tail):
    return 'LEFT'
  if (x_diff > 0 and direction != 'LEFT' and (pos[0] + 1, pos[1]) not in tail):
    return 'RIGHT'
  if (y_diff < 0 and direction != 'DOWN' and (pos[0], pos[1] - 1) not in tail):
    return 'UP'
  if (y_diff > 0 and direction != 'UP' and (pos[0], pos[1] + 1) not in tail):
    return 'DOWN'

  if (x_diff == 0):
    if (direction != 'RIGHT' and (pos[0] - 1, pos[1]) not in tail):
      return 'LEFT'
    if (direction != 'LEFT' and (pos[0] + 1, pos[1]) not in tail):
      return 'RIGHT'
  if (y_diff == 0):
    if (direction != 'DOWN' and (pos[0], pos[1] - 1) not in tail):
      return 'UP'
    if (direction != 'UP' and (pos[0], pos[1] + 1) not in tail):
      return 'DOWN'
    
  if (direction != 'RIGHT' and (pos[0] - 1, pos[1]) not in tail):
    return 'LEFT'
  if (direction != 'LEFT' and (pos[0] + 1, pos[1]) not in tail):
    return 'RIGHT'
  if (direction != 'DOWN' and (pos[0], pos[1] - 1) not in tail):
    return 'UP'
  if (direction != 'UP' and (pos[0], pos[1] + 1) not in tail):
    return 'DOWN'
  
  return 'LEFT'
    
