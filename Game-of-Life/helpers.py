def update(board):
  height = len(board)
  width = len(board[0])

  neighbors = getNeighbors(board)

  for y in range(height):
    for x in range(width):
      if neighbors[y][x] == 3 or (neighbors[y][x] == 2 and board[y][x] == 1):
        board[y][x] = 1
      else:
        board[y][x] = 0
  

  return board


def getNeighbors(board):
  height = len(board)
  width = len(board[0])

  neighbors = [[0 for i in height] for j in width]

  for y in range(height):
    for x in range(width):
      rows = [y - 1, y, y + 1]
      columns = [x - 1, x, x + 1]
      if y == 0: rows = rows[1:]       
      if y == height - 1: rows = rows[:2]    
      if x == 0: columns = columns[1:]
      if x == width - 1: columns = columns[:2]
        
      count = 0
      for i in rows:
        for j in columns:
          if (i == y and j == x): continue
          if (board[i][j] == 1): count += 1
      
      neighbors[y][x] = count

  return neighbors
