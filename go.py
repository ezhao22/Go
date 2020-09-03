import numpy as np

map_matrix = np.zeros(1)

def generate_map(rows, cols):
    map_matrix = np.zeros((rows, cols))
    return map_matrix

def alter_map (map_matrix, x,y, num):
    map_matrix[x,y]=num

def occupied(map_matrix, x, y):
    if map_matrix[x][y]==1 or map_matrix[x][y]==2:
        occup=True
    else:
        occup=False
    return occup



def five_row(map_matrix, num, x_coor):
    counter = 0
    returned = False
    for i in range(map_matrix[0].size):
        if map_matrix[x_coor, i] == num:
            counter = counter + 1
            if counter == 5:
                returned = True
                return True
        else:
            counter = 0
    if returned == False:
        return False


def four_row(map_matrix, num, x_coor):
    counter = 0
    returned = False
    for i in range(len(map_matrix[0])):
        if map_matrix[x_coor, i] == num:
            counter = counter + 1
            if counter == 4:
                returned = True
                return True
        else:
            counter = 0
    if returned == False:
        return False


def three_row(map_matrix, num, x_coor):
    counter = 0
    returned = False
    for i in range(len(map_matrix[0])):
        if map_matrix[x_coor, i] == num:
            counter = counter + 1
            if counter == 3:
                returned = True
                return True
        else:
            counter = 0
    if returned == False:
        return False


def five_col(map_matrix, num, y_coor):
    counter = 0
    returned = False
    for i in range(len(map_matrix)):
        if map_matrix[i, y_coor] == num:
            counter = counter + 1
            if counter == 5:
                returned = True
                return True
        else:
            counter = 0
    if returned == False:
        return False


def four_col(map_matrix, num, y_coor):
    counter = 0
    returned = False
    for i in range(len(map_matrix)):
        if map_matrix[i, y_coor] == num:
            counter = counter + 1
            if counter == 5:
                returned = True
                return True
        else:
            counter = 0
    if returned == False:
        return False


def three_col(map_matrix, num, y_coor):
    counter = 0
    returned = False
    for i in range(len(map_matrix)):
        if map_matrix[i, y_coor] == num:
            counter = counter + 1
            if counter == 3:
                returned = True
                return True
        else:
            counter = 0
    if returned == False:
        return False


def five_diagonal_decreasing(map_matrix, num, x_coor, y_coor):
    returned = True
    for i in range(5):
        if map_matrix[x_coor + i, y_coor + i] == None or map_matrix[x_coor + i, y_coor + i] != num:
            returned = False
            return False
    if returned == True:
        return True


def four_diagonal_decreasing(map_matrix, num, x_coor, y_coor):
    returned = True
    for i in range(4):
        if map_matrix[x_coor + i, y_coor + i] == None or map_matrix[x_coor + i, y_coor + i] != num:
            returned = False
            return False
    if returned == True:
        return True


def three_diagonal_decreasing(map_matrix, num, x_coor, y_coor):
    returned = True
    for i in range(3):
        if map_matrix[x_coor + i, y_coor + i] == None or map_matrix[x_coor + i, y_coor + i] != num:
            returned = False
            return False
    if returned == True:
        return True


def five_diagonal_increasing(map_matrix, num, x_coor, y_coor):
    returned = True
    for i in range(5):
        if map_matrix[x_coor + i, y_coor - i] == None or map_matrix[x_coor + i, y_coor - i] != num:
            returned = False
            return False
    if returned == True:
        return True


def four_diagonal_increasing(map_matrix, num, x_coor, y_coor):
    returned = True
    for i in range(5):
        if map_matrix[x_coor + i, y_coor - i] == None or map_matrix[x_coor + i, y_coor - i] != num:
            returned = False
            return False
    if returned == True:
        return True


def three_diagonal_increasing(map_matrix, num, x_coor, y_coor):
    returned = True
    for i in range(5):
        if map_matrix[x_coor + i, y_coor - i] == None or map_matrix[x_coor + i, y_coor - i] != num:
            returned = False
            return False
    if returned == True:
        return True


def check_combinations(map_matrix, num):
    list = []

    for i in range(len(map_matrix)):
        if (five_row(map_matrix, num, i) == True):
            list.append(["R", i, "five_row"])
        elif (four_row(map_matrix, num, i) == True):
            list.append(["R", i, "four_row"])
        elif (three_row(map_matrix, num, i) == True):
            list.append(["R", i, "three_row"])

    for i in range(len(map_matrix[0])):
        if (five_col(map_matrix, num, i) == True):
            list.append(["C", i, "five_col"])
        elif (four_col(map_matrix, num, i) == True):
            list.append(["C", i, "four_col"])
        elif (three_col(map_matrix, num, i) == True):
            list.append(["C", i, "three_col"])

    for x in range(len(map_matrix[0])):
        for y in range(len(map_matrix)):
            if (five_diagonal_decreasing(map_matrix, num, x, y) == True):
                list.append(["R", x, "C", y, "five_diagonal_decreasing"])
            elif (four_diagonal_decreasing(map_matrix, num, x, y) == True):
                list.append(["R", x, "C", y, "four_diagonal_decreasing"])
            elif (three_diagonal_decreasing(map_matrix, num, x, y) == True):
                list.append(["R", x, "C", y, "three_diagonal_decreasing"])
            if (five_diagonal_increasing(map_matrix, num, x, len(map_matrix) - 1 - y) == True):
                list.append(["R", x, "C", len(map_matrix) - 1 - y, "five_diagonal_increasing"])
            elif (four_diagonal_increasing(map_matrix, num, x, len(map_matrix) - 1 - y) == True):
                list.append(["R", x, "C", len(map_matrix) - 1 - y, "four_diagonal_increasing"])
            elif (three_diagonal_increasing(map_matrix, num, x, len(map_matrix) - 1 - y) == True):
                list.append(["R", x, "C" + len(map_matrix) - 1 - y, "three_diagonal_increasing"])

    return list


def five_in_a_row(map_matrix, num):
    returned = False
    for i in range(len(map_matrix)):
        if (five_row(map_matrix, num, i) == True):
            returned = True
            return True

    for i in range(len(map_matrix[0])):
        if (five_col(map_matrix, num, i) == True):
            returned = True
            return True

    for x in range(len(map_matrix[0])):
        for y in range(len(map_matrix)):
            if (five_diagonal_decreasing(map_matrix, num, x, y) == True) or (five_diagonal_increasing(map_matrix, num, x, y) == True):
                returned = True
                return True

    if (returned == False):
        return False;


def four_in_a_row(map_matrix, num):
    returned = False
    for i in range(len(map_matrix)):
        if (four_row(map_matrix, num, i) == True):
            returned = True
            return True

    for i in range(len(map_matrix[0])):
        if (four_col(map_matrix, num, i) == True):
            returned = True
            return True

    for x in range(len(map_matrix[0])):
        for y in range(len(map_matrix)):
            if (four_diagonal_decreasing(map_matrix, num, x, y) == True) or (four_diagonal_increasing(map_matrix, num, x, y) == True):
                returned = True
                return True

    if (returned == False):
        return False;


def three_in_a_row(map_matrix, num):
    returned = False
    for i in range(len(map_matrix)):
        if (three_row(map_matrix, num, i) == True):
            returned = True
            return True

    for i in range(len(map_matrix[0])):
        if (three_col(map_matrix, num, i) == True):
            returned = True
            return True

    for x in range(len(map_matrix[0])):
        for y in range(len(map_matrix)):
            if (three_diagonal_decreasing(map_matrix, num, x, y) == True) or (three_diagonal_increasing(map_matrix, num, x, y) == True):
                returned = True
                return True

    if (returned == False):
        return False;
