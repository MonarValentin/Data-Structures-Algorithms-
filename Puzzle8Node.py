class Move:
   def __init__(self, row, col):
      self.row = row
      self.col = col

   def __str__(self):
      return "({0}, {1})".format(self.row, self.col)

SIZE = 3

class Puzzle8Node():
   def __init__(self, position, parent = None):
      # The name will be the square
      # The name should only contain the numbers 1 to 8 and a blank
      sorted_pos =" 12345678"
      assert "".join(sorted(position)) == sorted_pos
      self.position = position
      self.parent = parent
      self.score = 0
      self.depth = 0
      

   def __eq__(self, other):
      """Override the default Equals behavior"""
      if other == None:
         return False
      return self.position == other.position

   def __ne__(self, other):
      """Define a non-equality test"""
      return not self.__eq__(other)

   def get_parent(self): return self.parent

   def get_path(self):
      # Follow the parent to create the path
      path = []
      node = self
      while node != None:
         path.append(node)
         node = node.parent
      return path

   def heuristic(self, goal):
      # Manhattan
      # Insert code here.
      start = self.position 
      goal = goal.position
      if start == goal:
         return 0
      i = 0
      totalOutOfPlace = 0
      while i < len(start):
         if start[i] != goal[i] and start[i] != " ":
            totalOutOfPlace += move_calc(i, goal.index(start[i]))
         i +=1

      return totalOutOfPlace


   def __str__(self):
      s = "|"
      for i in range(SIZE):
         start = i * SIZE
         s += self.position[start:start + SIZE] + "|"
      s += " ({}+{})".format(self.depth, self.score)
      return s

   def __repr__(self):
      return str(self)

   def make_board(self, this_position):
      board = [ ['-' for c in range(SIZE)] for r in range(SIZE)]
      index = 0
      for row in range(SIZE):
         for col in range(SIZE):
            board[row][col] = this_position[index]
            index += 1

      return board

   def make_name(self, board):
      position = ''
      for row in range(SIZE):
         for col in range(SIZE):
            position += board[row][col]

      return position

   def get_blank(self, board):
      # Find the blank
      for row in range(SIZE):
         for col in range(SIZE):
            if board[row][col] == ' ':
               return Move(row, col)

      return None # Error, this shouldn't happen. 

   def get_children(self):
      # The children are just the moves.
      children = self.get_moves()
      # Add in the parent
      # (that would be myself!)
      for child in children:
         # Record the parent and the depth.
         child.parent = self
         child.depth = child.parent.depth + 1 # Child is one deeper than parent

      return children

   def get_moves(self):
      # The moves depend on the current board position
      # Lets make the board
      board = self.make_board(self.position)
      blank = self.get_blank(board)

      # Now make the moves. There could be 4
      moves = []
      if blank.col != 0:
         # LEFT
         board[blank.row][blank.col-1], board[blank.row][blank.col] = board[blank.row][blank.col], board[blank.row][blank.col-1]
         # Convert board to a name and append to moves
         moves.append(self.make_name(board))
         # swap back to undo the move
         board[blank.row][blank.col-1], board[blank.row][blank.col] = board[blank.row][blank.col], board[blank.row][blank.col-1]
      if blank.row != 0: # Can't move up if already at the top
         # UP
         # swap blank and position above it
         board[blank.row-1][blank.col], board[blank.row][blank.col] = board[blank.row][blank.col], board[blank.row-1][blank.col]
         # Convert board to a name and append to moves
         moves.append(self.make_name(board))
         board[blank.row-1][blank.col], board[blank.row][blank.col] = board[blank.row][blank.col], board[blank.row-1][blank.col]
      if blank.col != SIZE-1:
         # RIGHT
         board[blank.row][blank.col+1], board[blank.row][blank.col] = board[blank.row][blank.col], board[blank.row][blank.col+1]
         # Convert board to a name and append to moves
         moves.append(self.make_name(board))
         board[blank.row][blank.col+1], board[blank.row][blank.col] = board[blank.row][blank.col], board[blank.row][blank.col+1]
      if blank.row != SIZE - 1:
         # Down
         board[blank.row+1][blank.col], board[blank.row][blank.col] = board[blank.row][blank.col], board[blank.row+1][blank.col]
         # Convert board to a name and append to moves
         moves.append(self.make_name(board))
         board[blank.row+1][blank.col], board[blank.row][blank.col] = board[blank.row][blank.col], board[blank.row+1][blank.col]

      return [Puzzle8Node(move) for move in moves]



def move_calc(start, goal):
   row = abs((start % 3) - (goal % 3))
   column = abs((start // 3)-(goal //3))
   return row + column