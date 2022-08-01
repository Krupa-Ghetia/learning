def get_row_with_max_value(mat):
    i = 0
    j = len(mat[0]) - 1
    result = None

    while j > -1 and i < len(mat):
        if mat[i][j] == 1:
            result = i
            j -= 1
        elif mat[i][j] == 0:
            i += 1

    print(result)


if __name__ == "__main__":
    get_row_with_max_value([[0, 0, 1, 1], [0, 0, 1, 1], [0, 1, 1, 1], [0, 0, 0, 0]])
    get_row_with_max_value([[0, 1, 1, 1, 1, 1], [0, 0, 1, 1, 1, 1], [0, 0, 0, 0, 0, 1], [0, 0, 0, 1, 1, 1]])
    get_row_with_max_value(
        [[0, 0, 0, 1, 1], [0, 0, 1, 1, 1], [0, 0, 0, 0, 1], [0, 0, 0, 0, 1], [0, 1, 1, 1, 1], [0, 0, 0, 1, 1],
         [0, 1, 1, 1, 1], [1, 1, 1, 1, 1]])
    get_row_with_max_value([[0, 0, 0, 1], [0, 0, 1, 1], [0, 1, 1, 1], [1, 1, 1, 1]])
    get_row_with_max_value([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1]])
    get_row_with_max_value([[0, 0, 0, 0], [0, 0, 1, 1], [0, 0, 0, 0], [0, 0, 0, 1], [0, 1, 1, 1]])
