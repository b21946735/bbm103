
import sys

f = open(sys.argv[1], "r")
commands = [[line.split()] for line in f.readlines()]
f.close()
def get_key(val):
    for key, value in board_dict.items():
         if val == value:
             return key

def turn_into_dict(liste):
    board_list = ""
    for i in liste:
        board_list = board_list + board_dict[f'{list(i)[0]} {list(i)[2]}']
        board_list = board_list + " "
    board_list = sorted(board_list.split())
    return board_list
def check_square(team, index):  # Check square is there enemy pieces
    return index in team


def find_piece_position(piece2):  # Takes pieces for find location
    return [(i, j.index(piece2)) for i, j in enumerate(chess_board) if piece2 in j]
def print_last_board():
    for i in chess_board:
        print(' '.join([str(aa) for aa in i]))
def initialize():  # Restart chess board
    global chess_board
    chess_board = [['R1', 'N1', 'B1', 'QU', 'KI', 'B2', 'N2', 'R2'], ['P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8'],
                   ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '], ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
                   ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '], ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
                   ['p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8'], ['r1', 'n1', 'b1', 'qu', 'ki', 'b2', 'n2', 'r2']]
    print_last_board()
    #for i in chess_board:
    #    print(' '.join([str(aa) for aa in i]))

def showmoves(piece) : #Takes pieces for show possible moves
    list_of_possible_moves.clear()
    pos = find_piece_position(piece)
    if list(piece)[0] == 'p': # Check up side for white pawn
        if pos[0][0] != 7:
            if chess_board[pos[0][0] - 1][pos[0][1]] == '  ' or check_square(black_team, chess_board[pos[0][0] - 1][pos[0][1]]) == True:
                list_of_possible_moves.append(f'{pos[0][0] - 1} {pos[0][1]}')
    elif list(piece)[0] == 'P': # Check down side for black pawn
        if pos[0][0] != 0:
            if chess_board[pos[0][0] + 1][pos[0][1]] == '  ' or check_square(white_team, chess_board[pos[0][0] + 1][pos[0][1]]) == True:
                list_of_possible_moves.append(f'{pos[0][0] + 1} {pos[0][1]}')
    elif list(piece)[0] == 'k':
        if pos[0][0] != 0:
            if chess_board[pos[0][0] - 1][pos[0][1]] == '  ' or check_square(black_team, chess_board[pos[0][0] - 1][pos[0][1]]) == True: # Check up side for white  king
                list_of_possible_moves.append(f'{pos[0][0] - 1} {pos[0][1]}')
            if pos[0][1] != 0:
                if chess_board[pos[0][0]-1][pos[0][1]-1] == '  ' or check_square(black_team,chess_board[pos[0][0]-1][pos[0][1]-1]) == True: # Check up left side for white king
                    list_of_possible_moves.append(f'{pos[0][0]-1} {pos[0][1]-1}')
            if pos[0][1] != 7:
                if chess_board[pos[0][0]-1][pos[0][1]+1] == '  ' or check_square(black_team,chess_board[pos[0][0]-1][pos[0][1]+1]) == True: # Check up right side for white king
                    list_of_possible_moves.append(f'{pos[0][0]-1} {pos[0][1]+1}')
        if pos[0][0] != 7:
            if chess_board[pos[0][0] + 1][pos[0][1]] == '  ' or check_square(black_team, chess_board[pos[0][0] + 1][pos[0][1]]) == True: # Check down side for white king
                list_of_possible_moves.append(f'{pos[0][0] + 1} {pos[0][1]}')
            if pos[0][1] != 0:
                if chess_board[pos[0][0]+1][pos[0][1]-1] == '  ' or check_square(black_team,chess_board[pos[0][0]+1][pos[0][1]-1]) == True: # Check down left side for white king
                    list_of_possible_moves.append(f'{pos[0][0]+1} {pos[0][1]-1}')
            if pos[0][1] != 7:
                if chess_board[pos[0][0]+1][pos[0][1]+1] == '  ' or check_square(black_team,chess_board[pos[0][0]+1][pos[0][1]+1]) == True: # Check down right side for white king
                    list_of_possible_moves.append(f'{pos[0][0]+1} {pos[0][1]+1}')
        if pos[0][1] !=0:
            if chess_board[pos[0][0]][pos[0][1]-1] == '  ' or check_square(black_team,chess_board[pos[0][0]][pos[0][1]-1]) == True: # Check left side for white king
                list_of_possible_moves.append(f'{pos[0][0]} {pos[0][1]-1}')
        if pos[0][1] !=7:
            if chess_board[pos[0][0]][pos[0][1]+1] == '  ' or check_square(black_team,chess_board[pos[0][0]][pos[0][1]+1]) == True: # Check right side for white king
                list_of_possible_moves.append(f'{pos[0][0]} {pos[0][1]+1}')
    elif list(piece)[0] == 'K':
        if pos[0][0] != 0:
            if chess_board[pos[0][0] - 1][pos[0][1]] == '  ' or check_square(white_team, chess_board[pos[0][0] - 1][pos[0][1]]) == True: # Check up side for black  king
                list_of_possible_moves.append(f'{pos[0][0] - 1} {pos[0][1]}')
            if pos[0][1] != 0:
                if chess_board[pos[0][0]-1][pos[0][1]-1] == '  ' or check_square(white_team,chess_board[pos[0][0]-1][pos[0][1]-1]) == True: # Check up left side for black king
                    list_of_possible_moves.append(f'{pos[0][0]-1} {pos[0][1]-1}')
            if pos[0][1] != 7:
                if chess_board[pos[0][0]-1][pos[0][1]+1] == '  ' or check_square(white_team,chess_board[pos[0][0]-1][pos[0][1]+1]) == True: # Check up right side for black king
                    list_of_possible_moves.append(f'{pos[0][0]-1} {pos[0][1]+1}')
        if pos[0][0] != 7:
            if chess_board[pos[0][0] + 1][pos[0][1]] == '  ' or check_square(white_team, chess_board[pos[0][0] + 1][pos[0][1]]) == True: # Check down side for black king
                list_of_possible_moves.append(f'{pos[0][0] + 1} {pos[0][1]}')
            if pos[0][1] != 0:
                if chess_board[pos[0][0]+1][pos[0][1]-1] == '  ' or check_square(white_team,chess_board[pos[0][0]+1][pos[0][1]-1]) == True: # Check down left side for black king
                    list_of_possible_moves.append(f'{pos[0][0]+1} {pos[0][1]-1}')
            if pos[0][1] != 7:
                if chess_board[pos[0][0]+1][pos[0][1]+1] == '  ' or check_square(white_team,chess_board[pos[0][0]+1][pos[0][1]+1]) == True: # Check down right side for black king
                    list_of_possible_moves.append(f'{pos[0][0]+1} {pos[0][1]+1}')
        if pos[0][1] !=0:
            if chess_board[pos[0][0]][pos[0][1]-1] == '  ' or check_square(white_team,chess_board[pos[0][0]][pos[0][1]-1]) == True: # Check left side for black king
                list_of_possible_moves.append(f'{pos[0][0]} {pos[0][1]-1}')
        if pos[0][1] !=7:
            if chess_board[pos[0][0]][pos[0][1]+1] == '  ' or check_square(white_team,chess_board[pos[0][0]][pos[0][1]+1]) == True: # Check right side for black king
                list_of_possible_moves.append(f'{pos[0][0]} {pos[0][1]+1}')
    elif list(piece)[0] == 'r':
        for i in range(1,pos[0][1]+1): # Check left side for white rook
            if chess_board[pos[0][0]][pos[0][1]-i] == '  ':
                list_of_possible_moves.append(f'{pos[0][0]} {pos[0][1]-i}')
            elif check_square(black_team,chess_board[pos[0][0]][pos[0][1]-i]) == True:
                list_of_possible_moves.append(f'{pos[0][0]} {pos[0][1]-i}')
                break
            else:
                break
        for i in range(1,8-pos[0][0]): # Check down side for white rook
            if chess_board[pos[0][0]+i][pos[0][1]] == '  ':
                list_of_possible_moves.append(f'{pos[0][0]+i} {pos[0][1]}')
            elif check_square(black_team,chess_board[pos[0][0]+i][pos[0][1]]) == True:
                list_of_possible_moves.append(f'{pos[0][0]+i} {pos[0][1]}')
                break
            else:
                break
        for i in range(1,pos[0][0]+1): # Check up side for white rook
            if chess_board[pos[0][0]-i][pos[0][1]] == '  ':
                list_of_possible_moves.append(f'{pos[0][0]-i} {pos[0][1]}')
            elif check_square(black_team,chess_board[pos[0][0]-i][pos[0][1]]) == True:
                list_of_possible_moves.append(f'{pos[0][0]-i} {pos[0][1]}')
                break
            else:
                break
        for i in range(1,8-pos[0][1]): # Check right side for white rook
            if chess_board[pos[0][0]][pos[0][1]+i] == '  ':
                list_of_possible_moves.append(f'{pos[0][0]} {pos[0][1]+i}')
            elif check_square(black_team,chess_board[pos[0][0]][pos[0][1]+i]) == True:
                list_of_possible_moves.append(f'{pos[0][0]} {pos[0][1]+i}')
                break
            else:
                break
    elif list(piece)[0] == 'R':
        for i in range(1,pos[0][1]+1): # Check left side for black rook
            if chess_board[pos[0][0]][pos[0][1]-i] == '  ':
                list_of_possible_moves.append(f'{pos[0][0]} {pos[0][1]-i}')
            elif check_square(white_team,chess_board[pos[0][0]][pos[0][1]-i]) == True:
                list_of_possible_moves.append(f'{pos[0][0]} {pos[0][1]-i}')
                break
            else:
                break
        for i in range(1,8-pos[0][0]): # Check down side for black rook
            if chess_board[pos[0][0]+i][pos[0][1]] == '  ':
                list_of_possible_moves.append(f'{pos[0][0]+i} {pos[0][1]}')
            elif check_square(white_team,chess_board[pos[0][0]+i][pos[0][1]]) == True:
                list_of_possible_moves.append(f'{pos[0][0]+i} {pos[0][1]}')
                break
            else:
                break
        for i in range(1,pos[0][0]+1): # Check up side for black rook
            if chess_board[pos[0][0]-i][pos[0][1]] == '  ':
                list_of_possible_moves.append(f'{pos[0][0]-i} {pos[0][1]}')
            elif check_square(white_team,chess_board[pos[0][0]-i][pos[0][1]]) == True:
                list_of_possible_moves.append(f'{pos[0][0]-i} {pos[0][1]}')
                break
            else:
                break
        for i in range(1,8-pos[0][1]): # Check right side for black rook
            if chess_board[pos[0][0]][pos[0][1]+i] == '  ':
                list_of_possible_moves.append(f'{pos[0][0]} {pos[0][1]+i}')
            elif check_square(white_team,chess_board[pos[0][0]][pos[0][1]+i]) == True:
                list_of_possible_moves.append(f'{pos[0][0]} {pos[0][1]+i}')
                break
            else:
                break
    elif list(piece)[0] == 'b':
        for i in range(1,min(int(pos[0][0]),int(pos[0][1]))+1): # Check up left side for white bishop
            if chess_board[pos[0][0]-i][pos[0][1]-i] == '  ':
                list_of_possible_moves.append(f'{pos[0][0]-i} {pos[0][1]-i}')
            elif check_square(black_team,chess_board[pos[0][0]-i][pos[0][1]-i]) == True:
                list_of_possible_moves.append(f'{pos[0][0]-i} {pos[0][1]-i}')
                break
            else:
                break
        for i in range(1,min(int(pos[0][0]),7-int(pos[0][1]))+1): # Check up right side for white bishop
            if chess_board[pos[0][0]-i][pos[0][1]+i] == '  ':
                list_of_possible_moves.append(f'{pos[0][0]-i} {pos[0][1]+i}')
            elif check_square(black_team,chess_board[pos[0][0]-i][pos[0][1]+i]) == True:
                list_of_possible_moves.append(f'{pos[0][0]-i} {pos[0][1]+i}')
                break
            else:
                break
    elif list(piece)[0] == 'B':
        for i in range(1,min(7-int(pos[0][0]),int(pos[0][1]))+1): # Check down left side for black bishop
            if chess_board[pos[0][0]+i][pos[0][1]-i] == '  ':
                list_of_possible_moves.append(f'{pos[0][0]+i} {pos[0][1]-i}')
            elif check_square(white_team,chess_board[pos[0][0]+i][pos[0][1]-i]) == True:
                list_of_possible_moves.append(f'{pos[0][0]+i} {pos[0][1]-i}')
                break
            else:
                break
        for i in range(1,min(7-int(pos[0][0]),7-int(pos[0][1]))+1): # Check down right side for black bishop
            if chess_board[pos[0][0]+i][pos[0][1]+i] == '  ':
                list_of_possible_moves.append(f'{pos[0][0]+i} {pos[0][1]+i}')
            elif check_square(white_team,chess_board[pos[0][0]+i][pos[0][1]+i]) == True:
                list_of_possible_moves.append(f'{pos[0][0]+i} {pos[0][1]+i}')
                break
            else:
                break
    elif list(piece)[0] == 'q':
        for i in range(1,pos[0][1]+1): # Check left side for white queen
            if chess_board[pos[0][0]][pos[0][1]-i] == '  ':
                list_of_possible_moves.append(f'{pos[0][0]} {pos[0][1]-i}')
            elif check_square(black_team,chess_board[pos[0][0]][pos[0][1]-i]) == True:
                list_of_possible_moves.append(f'{pos[0][0]} {pos[0][1]-i}')
                break
            else:
                break
        for i in range(1,8-pos[0][0]): # Check down side for white queen
            if chess_board[pos[0][0]+i][pos[0][1]] == '  ':
                list_of_possible_moves.append(f'{pos[0][0]+i} {pos[0][1]}')
            elif check_square(black_team,chess_board[pos[0][0]+i][pos[0][1]]) == True:
                list_of_possible_moves.append(f'{pos[0][0]+i} {pos[0][1]}')
                break
            else:
                break
        for i in range(1,pos[0][0]+1): # Check up side for white queen
            if chess_board[pos[0][0]-i][pos[0][1]] == '  ':
                list_of_possible_moves.append(f'{pos[0][0]-i} {pos[0][1]}')
            elif check_square(black_team,chess_board[pos[0][0]-i][pos[0][1]]) == True:
                list_of_possible_moves.append(f'{pos[0][0]-i} {pos[0][1]}')
                break
            else:
                break
        for i in range(1,8-pos[0][1]): # Check right side for white queen
            if chess_board[pos[0][0]][pos[0][1]+i] == '  ':
                list_of_possible_moves.append(f'{pos[0][0]} {pos[0][1]+i}')
            elif check_square(black_team,chess_board[pos[0][0]][pos[0][1]+i]) == True:
                list_of_possible_moves.append(f'{pos[0][0]} {pos[0][1]+i}')
                break
            else:
                break
        for i in range(1,min(7-int(pos[0][0]),int(pos[0][1]))+1): # Check down left side for white queen
            if chess_board[pos[0][0]+i][pos[0][1]-i] == '  ':
                list_of_possible_moves.append(f'{pos[0][0]+i} {pos[0][1]-i}')
            elif check_square(black_team,chess_board[pos[0][0]+i][pos[0][1]-i]) == True:
                list_of_possible_moves.append(f'{pos[0][0]+i} {pos[0][1]-i}')
                break
            else:
                break
        for i in range(1,min(int(pos[0][0]),int(pos[0][1]))+1): # Check up left side for white queen
            if chess_board[pos[0][0]-i][pos[0][1]-i] == '  ':
                list_of_possible_moves.append(f'{pos[0][0]-i} {pos[0][1]-i}')
            elif check_square(black_team,chess_board[pos[0][0]-i][pos[0][1]-i]) == True:
                list_of_possible_moves.append(f'{pos[0][0]-i} {pos[0][1]-i}')
                break
            else:
                break
        for i in range(1,min(7-int(pos[0][0]),7-int(pos[0][1]))+1): # Check down right side for white queen
            if chess_board[pos[0][0]+i][pos[0][1]+i] == '  ':
                list_of_possible_moves.append(f'{pos[0][0]+i} {pos[0][1]+i}')
            elif check_square(black_team,chess_board[pos[0][0]+i][pos[0][1]+i]) == True:
                list_of_possible_moves.append(f'{pos[0][0]+i} {pos[0][1]+i}')
                break
            else:
                break
        for i in range(1,min(int(pos[0][0]),7-int(pos[0][1]))+1): # Check up right side for black queen
            if chess_board[pos[0][0]-i][pos[0][1]+i] == '  ':
                list_of_possible_moves.append(f'{pos[0][0]-i} {pos[0][1]+i}')
            elif check_square(black_team,chess_board[pos[0][0]-i][pos[0][1]+i]) == True:
                list_of_possible_moves.append(f'{pos[0][0]-i} {pos[0][1]+i}')
                break
            else:
                break
    elif list(piece)[0] == 'Q':
        for i in range(1,pos[0][1]+1): # Check left side for black queen
            if chess_board[pos[0][0]][pos[0][1]-i] == '  ':
                list_of_possible_moves.append(f'{pos[0][0]} {pos[0][1]-i}')
            elif check_square(white_team,chess_board[pos[0][0]][pos[0][1]-i]) == True:
                list_of_possible_moves.append(f'{pos[0][0]} {pos[0][1]-i}')
                break
            else:
                break
        for i in range(1,8-pos[0][0]): # Check down side for black queen
            if chess_board[pos[0][0]+i][pos[0][1]] == '  ':
                list_of_possible_moves.append(f'{pos[0][0]+i} {pos[0][1]}')
            elif check_square(white_team,chess_board[pos[0][0]+i][pos[0][1]]) == True:
                list_of_possible_moves.append(f'{pos[0][0]+i} {pos[0][1]}')
                break
            else:
                break
        for i in range(1,pos[0][0]+1): # Check up side for black queen
            if chess_board[pos[0][0]-i][pos[0][1]] == '  ':
                list_of_possible_moves.append(f'{pos[0][0]-i} {pos[0][1]}')
            elif check_square(white_team,chess_board[pos[0][0]-i][pos[0][1]]) == True:
                list_of_possible_moves.append(f'{pos[0][0]-i} {pos[0][1]}')
                break
            else:
                break
        for i in range(1,8-pos[0][1]): # Check right side for black queen
            if chess_board[pos[0][0]][pos[0][1]+i] == '  ':
                list_of_possible_moves.append(f'{pos[0][0]} {pos[0][1]+i}')
            elif check_square(white_team,chess_board[pos[0][0]][pos[0][1]+i]) == True:
                list_of_possible_moves.append(f'{pos[0][0]} {pos[0][1]+i}')
                break
            else:
                break
        for i in range(1,min(7-int(pos[0][0]),int(pos[0][1]))+1): # Check down left side for black queen
            if chess_board[pos[0][0]+i][pos[0][1]-i] == '  ':
                list_of_possible_moves.append(f'{pos[0][0]+i} {pos[0][1]-i}')
            elif check_square(white_team,chess_board[pos[0][0]+i][pos[0][1]-i]) == True:
                list_of_possible_moves.append(f'{pos[0][0]+i} {pos[0][1]-i}')
                break
            else:
                break
        for i in range(1,min(int(pos[0][0]),int(pos[0][1]))+1): # Check up left side for black queen
            if chess_board[pos[0][0]-i][pos[0][1]-i] == '  ':
                list_of_possible_moves.append(f'{pos[0][0]-i} {pos[0][1]-i}')
            elif check_square(white_team,chess_board[pos[0][0]-i][pos[0][1]-i]) == True:
                list_of_possible_moves.append(f'{pos[0][0]-i} {pos[0][1]-i}')
                break
            else:
                break
        for i in range(1,min(7-int(pos[0][0]),7-int(pos[0][1]))+1): # Check down right side for black queen
            if chess_board[pos[0][0]+i][pos[0][1]+i] == '  ':
                list_of_possible_moves.append(f'{pos[0][0]+i} {pos[0][1]+i}')
            elif check_square(white_team,chess_board[pos[0][0]+i][pos[0][1]+i]) == True:
                list_of_possible_moves.append(f'{pos[0][0]+i} {pos[0][1]+i}')
                break
            else:
                break
        for i in range(1,min(int(pos[0][0]),7-int(pos[0][1]))+1): # Check up right side for black queen
            if chess_board[pos[0][0]-i][pos[0][1]+i] == '  ':
                list_of_possible_moves.append(f'{pos[0][0]-i} {pos[0][1]+i}')
            elif check_square(white_team,chess_board[pos[0][0]-i][pos[0][1]+i]) == True:
                list_of_possible_moves.append(f'{pos[0][0]-i} {pos[0][1]+i}')
                break
            else:
                break
    elif list(piece)[0] == 'n':
        if pos[0][0] != 0:
            if pos[0][1] != 0:
                if chess_board[pos[0][0]-1][pos[0][1]-1] == '  ' : # Check up left side for white knight
                    list_of_possible_moves.append(f'{pos[0][0]-1} {pos[0][1]-1}')
            if pos[0][1] != 7:
                if chess_board[pos[0][0]-1][pos[0][1]+1] == '  ' : # Check up right side for white knight
                    list_of_possible_moves.append(f'{pos[0][0]-1} {pos[0][1]+1}')
        if pos[0][0] != 7:
            if pos[0][1] != 0:
                if chess_board[pos[0][0]+1][pos[0][1]-1] == '  ' : # Check down left side for white knight
                    list_of_possible_moves.append(f'{pos[0][0]+1} {pos[0][1]-1}')
            if pos[0][1] != 7:
                if chess_board[pos[0][0]+1][pos[0][1]+1] == '  ' : # Check down right side for white knight
                    list_of_possible_moves.append(f'{pos[0][0]+1} {pos[0][1]+1}')
        if pos[0][0] != 1 and pos[0][1] != 0 and pos[0][0] != 0 and pos[0][1] != 0 :
            if chess_board[pos[0][0]-2][pos[0][1]-1] == '  ' or check_square(black_team,chess_board[pos[0][0]-2][pos[0][1]-1]) == True: # Check up up left side for white knight
                list_of_possible_moves.append(f'{pos[0][0]-2} {pos[0][1]-1}')
        if pos[0][0] != 1 and pos[0][1] != 7 and pos[0][0] != 0 and pos[0][1] != 7 :
            if chess_board[pos[0][0]-2][pos[0][1]+1] == '  ' or check_square(black_team,chess_board[pos[0][0]-2][pos[0][1]+1]) == True: # Check up up right side for white knight
                list_of_possible_moves.append(f'{pos[0][0]-2} {pos[0][1]+1}')
        if pos[0][0] != 0 and pos[0][1] != 0 and pos[0][0] != 0 and pos[0][1] != 1 :
            if chess_board[pos[0][0]-1][pos[0][1]-2] == '  ' or check_square(black_team,chess_board[pos[0][0]-1][pos[0][1]-2]) == True: # Check up left left side for white knight
                list_of_possible_moves.append(f'{pos[0][0]-1} {pos[0][1]-2}')
        if pos[0][0] != 0 and pos[0][1] != 7 and pos[0][0] != 0 and pos[0][1] != 6 :
            if chess_board[pos[0][0]-1][pos[0][1]+2] == '  ' or check_square(black_team,chess_board[pos[0][0]-1][pos[0][1]+2]) == True: # Check up right right side for white knight
                list_of_possible_moves.append(f'{pos[0][0]-1} {pos[0][1]+2}')
        if pos[0][0] != 7 and pos[0][1] != 0 and pos[0][0] != 6 and pos[0][1] != 0 :
            if chess_board[pos[0][0]+2][pos[0][1]-1] == '  ' or check_square(black_team,chess_board[pos[0][0]+2][pos[0][1]-1]) == True: # Check down down left side for white knight
                list_of_possible_moves.append(f'{pos[0][0]+2} {pos[0][1]-1}')
        if pos[0][0] != 7 and pos[0][1] != 7 and pos[0][0] != 6 and pos[0][1] != 7 :
            if chess_board[pos[0][0]+2][pos[0][1]+1] == '  ' or check_square(black_team,chess_board[pos[0][0]+2][pos[0][1]+1]) == True: # Check down down right side for white knight
                list_of_possible_moves.append(f'{pos[0][0]+2} {pos[0][1]+1}')
        if pos[0][0] != 7 and pos[0][1] != 0 and pos[0][0] != 7 and pos[0][1] != 1 :
            if chess_board[pos[0][0]+1][pos[0][1]-2] == '  ' or check_square(black_team,chess_board[pos[0][0]+1][pos[0][1]-2]) == True: # Check down left left side for white knight
                list_of_possible_moves.append(f'{pos[0][0]+1} {pos[0][1]-2}')
        if pos[0][0] != 7 and pos[0][1] != 7 and pos[0][0] != 7 and pos[0][1] != 6 :
            if chess_board[pos[0][0]+1][pos[0][1]+2] == '  ' or check_square(black_team,chess_board[pos[0][0]+1][pos[0][1]+2]) == True: # Check down right right side for white knight
                list_of_possible_moves.append(f'{pos[0][0]+1} {pos[0][1]+2}')
    elif list(piece)[0] == 'N':
        if pos[0][0] != 0:
            if pos[0][1] != 0:
                if chess_board[pos[0][0]-1][pos[0][1]-1] == '  ' : # Check up left side for black knight
                    list_of_possible_moves.append(f'{pos[0][0]-1} {pos[0][1]-1}')
            if pos[0][1] != 7:
                if chess_board[pos[0][0]-1][pos[0][1]+1] == '  ' : # Check up right side for black knight
                    list_of_possible_moves.append(f'{pos[0][0]-1} {pos[0][1]+1}')
        if pos[0][0] != 7:
            if pos[0][1] != 0:
                if chess_board[pos[0][0]+1][pos[0][1]-1] == '  ' : # Check down left side for black knight
                    list_of_possible_moves.append(f'{pos[0][0]+1} {pos[0][1]-1}')
            if pos[0][1] != 7:
                if chess_board[pos[0][0]+1][pos[0][1]+1] == '  ' : # Check down right side for black knight
                    list_of_possible_moves.append(f'{pos[0][0]+1} {pos[0][1]+1}')
        if pos[0][0] != 1 and pos[0][1] != 0 and pos[0][0] != 0 and pos[0][1] != 0 :
            if chess_board[pos[0][0]-2][pos[0][1]-1] == '  ' or check_square(white_team,chess_board[pos[0][0]-2][pos[0][1]-1]) == True: # Check up up left side for black knight
                list_of_possible_moves.append(f'{pos[0][0]-2} {pos[0][1]-1}')
        if pos[0][0] != 1 and pos[0][1] != 7 and pos[0][0] != 0 and pos[0][1] != 7 :
            if chess_board[pos[0][0]-2][pos[0][1]+1] == '  ' or check_square(white_team,chess_board[pos[0][0]-2][pos[0][1]+1]) == True: # Check up up right side for black knight
                list_of_possible_moves.append(f'{pos[0][0]-2} {pos[0][1]+1}')
        if pos[0][0] != 0 and pos[0][1] != 0 and pos[0][0] != 0 and pos[0][1] != 1 :
            if chess_board[pos[0][0]-1][pos[0][1]-2] == '  ' or check_square(white_team,chess_board[pos[0][0]-1][pos[0][1]-2]) == True: # Check up left left side for black knight
                list_of_possible_moves.append(f'{pos[0][0]-1} {pos[0][1]-2}')
        if pos[0][0] != 0 and pos[0][1] != 7 and pos[0][0] != 0 and pos[0][1] != 6 :
            if chess_board[pos[0][0]-1][pos[0][1]+2] == '  ' or check_square(white_team,chess_board[pos[0][0]-1][pos[0][1]+2]) == True: # Check up right right side for black knight
                list_of_possible_moves.append(f'{pos[0][0]-1} {pos[0][1]+2}')
        if pos[0][0] != 7 and pos[0][1] != 0 and pos[0][0] != 6 and pos[0][1] != 0 :
            if chess_board[pos[0][0]+2][pos[0][1]-1] == '  ' or check_square(white_team,chess_board[pos[0][0]+2][pos[0][1]-1]) == True: # Check down down left side for black knight
                list_of_possible_moves.append(f'{pos[0][0]+2} {pos[0][1]-1}')
        if pos[0][0] != 7 and pos[0][1] != 7 and pos[0][0] != 6 and pos[0][1] != 7 :
            if chess_board[pos[0][0]+2][pos[0][1]+1] == '  ' or check_square(white_team,chess_board[pos[0][0]+2][pos[0][1]+1]) == True: # Check down down right side for black knight
                list_of_possible_moves.append(f'{pos[0][0]+2} {pos[0][1]+1}')
        if pos[0][0] != 7 and pos[0][1] != 0 and pos[0][0] != 7 and pos[0][1] != 1 :
            if chess_board[pos[0][0]+1][pos[0][1]-2] == '  ' or check_square(white_team,chess_board[pos[0][0]+1][pos[0][1]-2]) == True: # Check down left left side for black knight
                list_of_possible_moves.append(f'{pos[0][0]+1} {pos[0][1]-2}')
        if pos[0][0] != 7 and pos[0][1] != 7 and pos[0][0] != 7 and pos[0][1] != 6 :
            if chess_board[pos[0][0]+1][pos[0][1]+2] == '  ' or check_square(white_team,chess_board[pos[0][0]+1][pos[0][1]+2]) == True: # Check down right right side for black knight
                list_of_possible_moves.append(f'{pos[0][0]+1} {pos[0][1]+2}')
    else:
        print('FAILED')
    return pos
chess_board = [['R1', 'N1', 'B1', 'QU', 'KI', 'B2', 'N2', 'R2'], ['P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8'],
               ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '], ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
               ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '], ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
               ['p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8'], ['r1', 'n1', 'b1', 'qu', 'ki', 'b2', 'n2', 'r2']]
black_team = ('R1', 'N1', 'B1', 'QU', 'B2', 'N2', 'R2', 'P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8')
white_team = ('p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8', 'r1', 'n1', 'b1', 'qu', 'b2', 'n2', 'r2')
board_dict = {'0 0': 'a8', '0 1': 'b8', '0 2': 'c8', '0 3': 'd8', '0 4': 'e8', '0 5': 'f8', '0 6': 'g8', '0 7': 'h8',
              '1 0': 'a7', '1 1': 'b7', '1 2': 'c7', '1 3': 'd7', '1 4': 'e7', '1 5': 'f7', '1 6': 'g7', '1 7': 'h7',
              '2 0': 'a6', '2 1': 'b6', '2 2': 'c6', '2 3': 'd6', '2 4': 'e6', '2 5': 'f6', '2 6': 'g6', '2 7': 'h6',
              '3 0': 'a5', '3 1': 'b5', '3 2': 'c5', '3 3': 'd5', '3 4': 'e5', '3 5': 'f5', '3 6': 'g5', '3 7': 'h5',
              '4 0': 'a4', '4 1': 'b4', '4 2': 'c4', '4 3': 'd4', '4 4': 'e4', '4 5': 'f4', '4 6': 'g4', '4 7': 'h4',
              '5 0': 'a3', '5 1': 'b3', '5 2': 'c3', '5 3': 'd3', '5 4': 'e3', '5 5': 'f3', '5 6': 'g3', '5 7': 'h3',
              '6 0': 'a2', '6 1': 'b2', '6 2': 'c2', '6 3': 'd2', '6 4': 'e2', '6 5': 'f2', '6 6': 'g2', '6 7': 'h2',
              '7 0': 'a1', '7 1': 'b1', '7 2': 'c1', '7 3': 'd1', '7 4': 'e1', '7 5': 'f1', '7 6': 'g1', '7 7': 'h1'}
list_of_possible_moves = []


for i in commands:
    a = i[0]
    if a[0]== 'move':
        print('> ',*a)
        b=showmoves(f'{a[1]}')
        if a[2] in turn_into_dict(list_of_possible_moves):
            print('OK')
            chess_board[int(list(get_key(a[2]))[0])][int(list(get_key(a[2]))[2])]=a[1]
            chess_board[int(list(b[0])[0])][int(list(b[0])[1])] = '  '
        else:
            print('FAILED')
    elif a[0]=='showmoves':
        print('> ',*a)
        showmoves(f'{a[1]}')
        if len(list(turn_into_dict(list_of_possible_moves))) == 0:
            print('FAILED')
        else:
            print(*turn_into_dict(list_of_possible_moves))
    elif a[0]=='initialize':
        print('> initialize')
        print('OK')
        print('-------------------------')
        initialize()
        print('-------------------------')
    elif a[0]=='print':
        print('> print')
        print('-------------------------')
        print_last_board()
        print('-------------------------')
    elif a[0]=='exit':
        print('> exit')
        exit()
