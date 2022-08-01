import math


def rotate_matrix(mat):
    mat = reverse_rows(mat)
    mat = reverse_columns(mat)

    print(mat)


def reverse_rows(mat):
    mat_len = len(mat)

    for i in range(0, mat_len):
        for j in range(0, math.floor(mat_len/2)):
            mat[i][j], mat[i][mat_len - j - 1] = mat[i][mat_len - j - 1], mat[i][j]

    return mat


def reverse_columns(mat):
    mat_len = len(mat)

    for j in range(0, mat_len):
        for i in range(0, math.floor(mat_len/2)):
            mat[i][j], mat[mat_len - i - 1][j] = mat[mat_len - i - 1][j], mat[i][j]

    return mat


if __name__ == "__main__":
    rotate_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    rotate_matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
