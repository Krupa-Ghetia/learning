def print_matrix_spirally(mat, rows, cols):
    left = 0
    right = cols - 1
    top = 0
    bottom = rows - 1

    for i in range(0, rows * cols):

        for j in range(left, right + 1):
            print(mat[top][j], end=" ")
        top = top + 1

        for j in range(top, bottom + 1):
            print(mat[j][right], end=" ")
        right = right - 1

        for j in range(right, left - 1, -1):
            print(mat[bottom][j], end=" ")
        bottom = bottom - 1

        for j in range(bottom, top - 1, -1):
            print(mat[j][left], end=" ")
        left = left + 1
    print("")


if __name__ == "__main__":
    print_matrix_spirally([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3, 3)
    print_matrix_spirally([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], 4, 4)
