import copy

input1 = list(input("Please enter feeding map as a list:"))
input2 = list(input("Please enter direction of movements as a list:"))
mid_variable1, mid_variable2 = input1.count("["), input1.count("'")
row_len = mid_variable1 - 1  # Calculate row length of board
column_len = int(mid_variable2 / (2 * row_len))  # Calculate column length of board
list1, instant_board, command_list, list3, end_score = [], [], [], [], 0

for i in input1:
    if i == 'X' or i == 'W' or i == 'A' or   i == 'C' or i == 'M' or i == 'P' or i == '*':
        list1.append(i)
for i in range(row_len):
    instant_board.append([])
    for j in list1[0 + column_len * i:column_len * (i + 1)]:
        instant_board[i].append(j)
for i in input2:
    if i == 'U' or i == 'D' or i == 'L' or i == 'R':
        command_list.append(i)
list_for_input_board = copy.deepcopy(instant_board)


def score(game_score=None):  # Function for calculate score
    global end_score
    if instant_board[rabbit_vertical][rabbit_horizontal] == 'C':
        end_score = game_score + 10
    elif instant_board[rabbit_vertical][rabbit_horizontal] == 'A':
        end_score = game_score + 5
    elif instant_board[rabbit_vertical][rabbit_horizontal] == 'M':
        end_score = game_score - 5
    elif instant_board[rabbit_vertical][rabbit_horizontal] == 'P':
        print("Your board is:")
        for i in list_for_input_board:  # Print input board
            table3 = ' '.join([str(aa) for aa in i])
            print(table3)
        print("Your output should be like this:")
        for i in instant_board:
            instant_board[rabbit_vertical][rabbit_horizontal] = '*'
            table2 = ' '.join([str(aa) for aa in i])
            print(table2)
        print('Your score is:', end_score)
        exit()
    return end_score


rabbit_position = [(i, j.index("*")) for i, j in enumerate(instant_board) if "*" in j]  # Find initial position of rabbit

rabbit_horizontal = rabbit_position[0][1]
rabbit_vertical = rabbit_position[0][0]
rows = len(instant_board[1])
for i in range(0, len(command_list)):
    if command_list[i] == 'L' and instant_board[rabbit_vertical][rabbit_horizontal - 1] != 'W':  # Move left when command is 'L'
        if rabbit_horizontal == 0:
            pass
        else:
            instant_board[rabbit_vertical][rabbit_horizontal] = 'X'
        if rabbit_horizontal > 0:
            rabbit_horizontal -= 1
            end_score = score(end_score)
            instant_board[rabbit_vertical][rabbit_horizontal] = '*'

    elif command_list[i] == 'R':  # Move right when command is 'R'
        if rabbit_horizontal == rows - 1:
            if instant_board[rabbit_vertical][rabbit_horizontal] != 'W':
                if rows > rabbit_horizontal + 1:
                    rabbit_horizontal += 1
                    end_score = score(end_score)
                    instant_board[rabbit_vertical][rabbit_horizontal] = '*'
        else:
            value = rabbit_horizontal
            if instant_board[rabbit_vertical][value + 1] != 'W':
                instant_board[rabbit_vertical][rabbit_horizontal] = 'X'
                if rows > rabbit_horizontal + 1:
                    rabbit_horizontal += 1
                    end_score = score(end_score)
                    instant_board[rabbit_vertical][rabbit_horizontal] = '*'
    elif command_list[i] == 'U' and instant_board[rabbit_vertical - 1][rabbit_horizontal] != 'W':  # Move Up when command is 'U'
        if rabbit_vertical == 0:
            pass
        else:
            instant_board[rabbit_vertical][rabbit_horizontal] = 'X'
        if rabbit_vertical > 0:
            rabbit_vertical -= 1
            end_score = score(end_score)
            instant_board[rabbit_vertical][rabbit_horizontal] = '*'

    elif command_list[i] == 'D':  # Move down when command is 'D'
        if rabbit_vertical == len(instant_board) - 1:
            if instant_board[rabbit_vertical][rabbit_horizontal] != 'W':
                if rabbit_vertical < len(instant_board) - 1:
                    rabbit_vertical += 1
                    end_score = score(end_score)
                    instant_board[rabbit_vertical][rabbit_horizontal] = '*'
        else:
            value = rabbit_vertical
            if instant_board[value + 1][rabbit_horizontal] != 'W':
                instant_board[rabbit_vertical][rabbit_horizontal] = 'X'
                if rabbit_vertical < len(instant_board) - 1:
                    rabbit_vertical += 1
                    end_score = score(end_score)
                    instant_board[rabbit_vertical][rabbit_horizontal] = '*'
print("Your board is:")
for i in list_for_input_board:  # Print input board
    table3 = ' '.join([str(aa) for aa in i])
    print(table3)
print("Your output should be like this:")
for i in instant_board:  # Print final board
    table = ' '.join([str(aa) for aa in i])
    print(table)

print('Your score is:', end_score)
