import sys
import os

try:
    def size_codes(codes_list):  # Divide codes according to key matrix size
        codes_list = [codes_list[aa:aa + matrix_size] for aa in range(0, len(codes_list), matrix_size)]
        return codes_list


    def matrix_multiple(code_list, matrix_key, size_matrix):
        bos_list = []
        asd = 0
        for i in code_list:
            for k in matrix_key:
                for j in range(size_matrix):
                    asd += i[j] * k[j]
                bos_list.append(asd)
                asd = 0
        return bos_list


    def decode():
        f2 = open(sys.argv[3], "r")
        decoded_list = []
        for i in f2.readlines():
            decoded_list = i.split(",")
        decoded_list = [int(i) for i in decoded_list]
        return decoded_list


    def list_to_string(empty_list):
        empty_list = [int(i) for i in empty_list]
        string = ','.join([str(u) for u in empty_list])
        return string


    def inverse_of_key():
        inverse_list = []
        x = 0
        unit_matrix = []
        for i in range(matrix_size):  # create unit matrix for take inverse of the key matrix
            for j in range(matrix_size):
                if j == i:
                    inverse_list.append(1)
                else:
                    inverse_list.append(0)
        while x < len(inverse_list):
            unit_matrix.append(inverse_list[x:x + matrix_size])
            x += matrix_size
        i = matrix_size - 1
        while i >= 0:  # take inverse o f key matrix
            if key_matrix[i][i] == 0:
                moment = key_matrix[i]
                key_matrix[i] = key_matrix[i - 1]
                key_matrix[i - 1] = moment
                moment = unit_matrix[i]
                unit_matrix[i] = unit_matrix[i - 1]
                unit_matrix[i - 1] = moment
            divisor = key_matrix[i][i]
            for j in range(matrix_size-1, -1, -1):
                key_matrix[i][j] /= divisor
                unit_matrix[i][j] /= divisor
            for k in range(matrix_size-1, -1, -1):
                if k == i:
                    pass
                else:
                    multiplier = key_matrix[k][i]
                    for h in range(matrix_size-1, -1, -1):
                        key_matrix[k][h] = round(key_matrix[k][h] - multiplier * key_matrix[i][h], 3)
                        unit_matrix[k][h] = round(unit_matrix[k][h] - multiplier * unit_matrix[i][h], 3)
            i -= 1
        unit_matrix = [[round(i, 1) for i in xx] for xx in unit_matrix]
        return unit_matrix


    def encode():  # add " " to end of the input text
        a = open(sys.argv[3], "r")
        numbers_list = []
        for i in a.readlines():
            for j in i.upper():
                numbers_list.append(my_dict[j])
        add_blank = len(numbers_list) % matrix_size
        for i in range(add_blank):
            numbers_list.append(int(27))
        return numbers_list


    last_list, key_matrix = [], []
    assert sys.argv[2][-3:] == "txt", "Key file could not be read error"  # Assertion for error 8
    assert sys.argv[3][-3:] == "txt", "Input file could not be read error"  # Assertion for error 4
    assert len(sys.argv) == 5, "Parameter number error"  # Assertion for error 1
    assert sys.argv[1] == "enc" or sys.argv[1] == "dec", "Undefined parameter error"  # Assertion for error 2
    file_size2 = os.path.getsize(sys.argv[2])
    assert file_size2 != 0, "Key file is empty error"  # Assertion for error 9
    file_size = os.path.getsize(sys.argv[3])
    assert file_size != 0, "Input file is empty error"  # Assertion for error 5
    my_dict = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9,
               "J": 10, "K": 11, "L": 12, "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18,
               "S": 19, "T": 20, "U": 21, "V": 22, "W": 23, "X": 24, "Y": 25, "Z": 26, " ": 27}
    f = open(sys.argv[2], "r")
    for i in f.readlines():
        i = i.split("\n")
        key_matrix = key_matrix + i
    key_matrix.remove("")
    key_matrix = [i.split(",") for i in key_matrix]
    matrix_size = len(key_matrix[0])
    for i in key_matrix:
        key_matrix = [xx for xx in key_matrix if xx != [""]]
    key_matrix = [list(map(int, i)) for i in key_matrix]
    if sys.argv[1] == "enc":
        xxx = open(sys.argv[4], "w")
        number_list = size_codes(encode())
        xxx.write(list_to_string(matrix_multiple(number_list, key_matrix, matrix_size)))

    elif sys.argv[1] == "dec":
        key_matrix = inverse_of_key()
        decode_list = size_codes(decode())
        abc = matrix_multiple(decode_list, key_matrix, matrix_size)
        abc = [int(i) for i in abc]
        for i in abc:
            last_list.append(list(my_dict.keys())[list(my_dict.values()).index(i)])
        yyy = open(sys.argv[4], "w")
        for j in last_list:
            yyy.write(str(j).rstrip('\n'))


except AssertionError as error:
    print(error)  # Assertions 1 2 5 9 8 4
except FileNotFoundError as error:
    if error.filename == sys.argv[2]:  # Assertions 3
        print("Key file not found error")
    else:  # Assertions 4
        print("Input file not found error")
except KeyError as error:  # Assertions 6
    print(f"Invalid character in input file error")
except:  # Assertions 10
    print("Invalid character in key file error")

