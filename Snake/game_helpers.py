import random

def move(tail, direction, length):
  pos = tail[-1]
  match direction:
    case 'UP':
      tail.append((pos[0], pos[1] - 1))
      if len(tail) > length:
        tail.pop(0)
    case 'DOWN':
      tail.append((pos[0], pos[1] + 1))
      if len(tail) > length:
        tail.pop(0)
    case 'LEFT':
      tail.append((pos[0] - 1, pos[1]))
      if len(tail) > length:
        tail.pop(0)
    case 'RIGHT':
      tail.append((pos[0] + 1, pos[1]))
      if len(tail) > length:
        tail.pop(0)
  return tail

def gen(GRID_WIDTH, GRID_HEIGHT):
  pos = (random.randint(1, GRID_WIDTH - 2), random.randint(2, GRID_HEIGHT - 2))
  tail = [pos]
  while True:
    apple_pos = (random.randint(0, GRID_WIDTH - 1), random.randint(1, GRID_HEIGHT - 1))
    if (apple_pos != pos): break
  return tail, apple_pos