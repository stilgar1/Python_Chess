def whitePiece():
    while True:
        inp = input('Choose position and piece for white: Rook, Pawn (Format E.g. Rook a1): ')
        # Lowercase the input string
        inp_lower = inp.lower()
        words = inp_lower.split(' ')
        
        # Check if the input has two words
        if len(words) != 2:
            print("Invalid input format. Please provide both piece and position.")
            continue
        
        # Check if the first word is 'rook' or 'pawn'
        if words[0] not in ['rook', 'pawn']:
            print("Invalid piece. Please choose either 'Rook' or 'Pawn'.")
            continue
        
        position = words[1]
        # Check if the position is in the correct format (e.g., 'a1')
        if len(position) != 2 or position[0] not in 'abcdefgh' or position[1] not in '12345678':
            print("Invalid position format. Please provide position in the format 'letternumber' (e.g., 'a1').")
            continue
        
        # Update the board with the chosen piece at the specified position
        row_index = 8 - int(position[1])
        col_index = ord(position[0]) - ord('a') + 1
        if board[row_index][col_index] != '-':
            print("Spot taken! Choose another position.")
            continue
        
        # Assign the piece based on the user's input
        piece = '♖' if words[0] == 'rook' else '♙'
        board[row_index][col_index] = piece

        print("Piece chosen:", piece)
        printBoard(board)

        # Return the position of the white piece
        return row_index, col_index, piece

def blackPiece():
    count = 0
    while count < 16:
        inp = input(f'Choose position for black pieces. Just coordinates. E.g., a2. When finished, print "done" {count+1}: ')
        
        if inp == 'done' and count == 0: # Check if the user input any piece
            print("You haven't selected any position")
            continue
        elif inp == 'done' and count > 0:
            printBoard(board)
            break
        else:
            # Check if the input is in the correct format (letternumber)
            if len(inp) != 2 or inp[0] not in 'abcdefgh' or inp[1] not in '12345678':
                print("Invalid position format. Please provide position in the format 'letternumber' (e.g., 'a1').")
                continue
            
            piece = '♟'  
            position = inp.lower()  
            row_index = 8 - int(position[1])
            col_index = ord(position[0]) - ord('a') + 1
            if board[row_index][col_index] != '-':  # Check if the spot is taken by a black or white piece
                print("Spot taken! Choose another position.")
                continue
        
            # Update the board with the black pawn at the specified position
            board[row_index][col_index] = piece
            count += 1
            printBoard(board)

def checkPawnCaptures(board, position): 
    """This is a function"""
    captures = []
    row, col = position

    # Determine the squares that the white pawn can capture
    capture_squares = [(row - 1, col - 1), (row - 1, col + 1)]

    # Check if any black pieces are present in the capture squares
    for new_row, new_col in capture_squares:
        if 0 <= new_row < 8 and 0 <= new_col < 8:  # Check if the position is within the board
            if board[new_row][new_col] == '♟':
                captures.append((new_row, new_col))

    return captures

def checkRookCaptures(board, position):
    captures = []
    row, col = position

    # Check captures along the same row
    for i in range(col - 1, -1, -1):  # Check left
        if board[row][i] == '♟':  
            captures.append((row, i))
            break
        elif board[row][i] != '-':
            break

    for i in range(col + 1, 9, +1):  # Check right
        if board[row][i] == '♟':  
            captures.append((row, i))
            break
        elif board[row][i] != '-':
            break

    # Check captures along the same column
    for i in range(row - 1, -1, -1):  # Check up
        if board[i][col] == '♟':  
            captures.append((i, col))
            break
        elif board[i][col] != '-':
            break

    for i in range(row + 1, 8, +1):  # Check down
        if board[i][col] == '♟':  
            captures.append((i, col))
            break
        elif board[i][col] != '-':
            break

    return captures

def printBoard(board):
    for row in board:
        print(' '.join(row))

board = [
    ['8', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['7', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['6', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['5', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['4', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['3', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['2', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['1', '-', '-', '-', '-', '-', '-', '-', '-'],
    [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
]

def matrix_to_chessboard(matrix_coords):
    chessboard_coords = []
    for row, col in matrix_coords:
        chess_row = 8 - row
        chess_col = chr((col + ord('a')) - 1)
        chessboard_coords.append(chess_col + str(chess_row))
    return chessboard_coords

def print_captures(possible_captures):
    chessboard_coordinates = matrix_to_chessboard(possible_captures)
    print("Possible captures:")
    if len(chessboard_coordinates) == 0:
        print("None")
    else:    
        for coord in chessboard_coordinates:
            print(coord)


whitePosition = whitePiece()

blackPiece()

if whitePosition[2] == '♙':
    possible_captures = checkPawnCaptures(board, (whitePosition[0], whitePosition[1]))
    print_captures(possible_captures)
else:
    possible_captures = checkRookCaptures(board, (whitePosition[0], whitePosition[1]))
    print_captures(possible_captures)
