def update(board):
  new_board = set()
  all_neighbors = set()

  for pos in board:
    neighbors = getNeighbors(pos)
    all_neighbors.update(neighbors)

    neighbors = list(filter(lambda x: x in board, neighbors))

    if (len(neighbors) in [2, 3]):
      new_board.add(pos)
  
  for pos in all_neighbors:
    neighbors = getNeighbors(pos)
    neighbors = list(filter(lambda x: x in board, neighbors))

    if (len(neighbors) == 3):
      new_board.add(pos)

  return new_board
     


def getNeighbors(pos):
  x, y = pos
  neighbors = []
  rows = [y - 1, y, y + 1]
  cols = [x - 1, x, x + 1]

  for row in rows:
    for col in cols:
      if row == y and col == x: continue
      neighbors.append((col, row))
  return neighbors
