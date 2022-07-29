def print_matrix_spirally(mat, rows, cols):
    left = 0
    right = cols - 1
    top = 0
    bottom = rows - 1
    visited_elems = 0

    while visited_elems < rows * cols:
        j = left
        while j <= right:
            print(mat[top][j], end=" ")
            j += 1
            visited_elems += 1
        top = top + 1

        j = top
        while j <= bottom:
            print(mat[j][right], end=" ")
            j += 1
            visited_elems += 1
        right = right - 1

        j = right
        while j >= left:
            print(mat[bottom][j], end=" ")
            j -= 1
            visited_elems += 1
        bottom = bottom - 1

        j = bottom
        while j >= top:
            print(mat[j][left], end=" ")
            j -= 1
            visited_elems += 1
        left = left + 1
    print("")


if __name__ == "__main__":
    print_matrix_spirally([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3, 3)
    print_matrix_spirally([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], 4, 4)
