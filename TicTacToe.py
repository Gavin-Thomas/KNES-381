# What did Gavin do?
  #ADDED ASCII ART
  #ADDED CLEARER INSTRUCTIONS ABOUT INPUTS (between 0 and 2, cuz that might trip people up)
  #ADDED SAFEGUARD FOR INPUT VALUES OVER 2 (MUST REDO THE INPUT)
  #ADDED OPTION TO PLAY THE GAME AGAIN ONCE FINISHED USING A WHILE LOOP
#Note: there are tons of more potential fixes for this game, but these are just a few I used

print('''
        88                                                              
  ,d    ""              ,d                            ,d                
  88                    88                            88                
MM88MMM 88  ,adPPYba, MM88MMM ,adPPYYba,  ,adPPYba, MM88MMM ,adPPYba,   
  88    88 a8"     ""   88    ""     `Y8 a8"     ""   88   a8"     "8a  
  88    88 8b           88    ,adPPPPP88 8b           88   8b       d8  
  88,   88 "8a,   ,aa   88,   88,    ,88 "8a,   ,aa   88,  "8a,   ,a8"  
  "Y888 88  `"Ybbd8"'   "Y888 `"8bbdP"Y8  `"Ybbd8"'   "Y888 `"YbbdP"' 
''')

# define the board
board = [["_" for i in range(3)] for j in range(3)]

# define the player's move
def make_move(board, player, row, col):
  board[row][col] = player

# define the function to check for a winner
def check_winner(board):
  # check rows
  for row in range(3):
    if board[row][0] == board[row][1] and board[row][1] == board[row][2] and board[row][0] != "_":
      return board[row][0]

  # check columns
  for col in range(3):
    if board[0][col] == board[1][col] and board[1][col] == board[2][col] and board[0][col] != "_":
      return board[0][col]

  # check diagonals
  if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != "_":
    return board[0][0]
  if board[2][0] == board[1][1] and board[1][1] == board[0][2] and board[2][0] != "_":
    return board[2][0]

  # if there is no winner, return None
  return None

# define the function to check if the game is a draw
def check_draw(board):
  for row in range(3):
    for col in range(3):
      if board[row][col] == "_":
        return False
  return True

# define the function to play the game
def play_game():
  # initialize the game
  player = "X"
  winner = None
  draw = False

  # loop until the game is over
  while not winner and not draw:
    # print the current board
    for row in board:
      print(" ".join(row))

    # GAVIN - Also added safeguard for inputting VALUES OVER 
    # get the player's move - (GAVIN - ADDED CLEARER INSTRUCTIONS ABOUT PYTHON SYNTAX FOR ZEROS)
    row = int(input("Enter row (0-2) note-highest row up is 0: "))
    if row >2:
      print("Try again.")
      row = int(input("Enter row (0-2) note-highest row up is 0: "))
    
    col = int(input("Enter column (0-2) note-farthest left column is 0: "))
    if col >2:
      print("Try again.")
      col = int(input("Enter column (0-2) note-farthest left column is 0: "))
    
    # make the move
    make_move(board, player, row, col)

    # check for a winner
    winner = check_winner(board)

    # check for a draw
    draw = check_draw(board)

    # switch players (Gavin - added lowercase x as well)
    if player == "X":
      player = "O"
    else:
      player = "X"

  # print the final board
  for row in board:
    print(" ".join(row))

  # print the result of the game 

  if winner:
    print(f"Player {winner} wins!")
  else:
    print("The game is a draw.")

play_game()

# (GAVIN - OPTION TO PLAY AGAIN!)

play_again = input("Would you like to play again? use capital Y or N ")

while play_again == "Y":

  print('''
          88                                                              
    ,d    ""              ,d                            ,d                
    88                    88                            88                
  MM88MMM 88  ,adPPYba, MM88MMM ,adPPYYba,  ,adPPYba, MM88MMM ,adPPYba,   
    88    88 a8"     ""   88    ""     `Y8 a8"     ""   88   a8"     "8a  
    88    88 8b           88    ,adPPPPP88 8b           88   8b       d8  
    88,   88 "8a,   ,aa   88,   88,    ,88 "8a,   ,aa   88,  "8a,   ,a8"  
    "Y888 88  `"Ybbd8"'   "Y888 `"8bbdP"Y8  `"Ybbd8"'   "Y888 `"YbbdP"' 
  ''')

  # define the board
  board = [["_" for i in range(3)] for j in range(3)]

  # define the player's move
  def make_move(board, player, row, col):
    board[row][col] = player

  # define the function to check for a winner
  def check_winner(board):
    # check rows
    for row in range(3):
      if board[row][0] == board[row][1] and board[row][1] == board[row][2] and board[row][0] != "_":
        return board[row][0]

    # check columns
    for col in range(3):
      if board[0][col] == board[1][col] and board[1][col] == board[2][col] and board[0][col] != "_":
        return board[0][col]

    # check diagonals
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != "_":
      return board[0][0]
    if board[2][0] == board[1][1] and board[1][1] == board[0][2] and board[2][0] != "_":
      return board[2][0]

    # if there is no winner, return None
    return None

  # define the function to check if the game is a draw
  def check_draw(board):
    for row in range(3):
      for col in range(3):
        if board[row][col] == "_":
          return False
    return True

  # define the function to play the game
  def play_game():
    # initialize the game
    player = "X"
    winner = None
    draw = False

    # loop until the game is over
    while not winner and not draw:
      # print the current board
      for row in board:
        print(" ".join(row))

      # get the player's move - (GAVIN - ADDED CLEARER INSTRUCTIONS ABOUT PYTHON SYNTAX FOR ZEROS)
      row = int(input("Enter row (0-2) note-highest row up is 0: "))
      col = int(input("Enter column (0-2) note-farthest left column is 0: "))

      # make the move
      make_move(board, player, row, col)

      # check for a winner
      winner = check_winner(board)

      # check for a draw
      draw = check_draw(board)

      # switch players (Gavin - added lowercase x as well)
      if player == "X":
        player = "O"
      else:
        player = "X"

    # print the final board
    for row in board:
      print(" ".join(row))

    # print the result of the game - (GAVIN - ADDED OPTION TO PLAY AGAIN!)
    if winner:
      print(f"Player {winner} wins!")
      play_again = input("Would you like to play again? use capital Y or N ")
    else:
      print("The game is a draw.")
      play_again

  play_game()

  #The end :)
