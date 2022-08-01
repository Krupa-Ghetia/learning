import math


def rotate_matrix_clockwise(mat):
    mat = transpose_matrtix(mat)
    mat = reverse_rows(mat)

    print(mat)


def transpose_matrtix(mat):

    for i in range(0, len(mat)):
        for j in range(i, len(mat)):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

    return mat


def reverse_rows(mat):

    mat_len = len(mat)
    for i in range(0, mat_len):
        for j in range(0, math.floor(mat_len/2)):
            mat[i][j], mat[i][mat_len - j - 1] = mat[i][mat_len - j - 1], mat[i][j]

    return mat


if __name__ == "__main__":
    rotate_matrix_clockwise([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    rotate_matrix_clockwise([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])

