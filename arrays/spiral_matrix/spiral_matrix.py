def print_matrix_spirally(mat, rows, cols):
    left = 0
    right = cols - 1
    top = 0
    bottom = rows - 1
    visited_elems = 0
    total_elems = rows * cols

    while visited_elems < total_elems:
        j = left
        while j <= right and visited_elems <total_elems:
            print(mat[top][j], end=" ")
            j += 1
            visited_elems += 1
        top = top + 1

        j = top
        while j <= bottom and visited_elems <total_elems:
            print(mat[j][right], end=" ")
            j += 1
            visited_elems += 1
        right = right - 1

        j = right
        while j >= left and visited_elems < total_elems:
            print(mat[bottom][j], end=" ")
            j -= 1
            visited_elems += 1
        bottom = bottom - 1

        j = bottom
        while j >= top and visited_elems < total_elems:
            print(mat[j][left], end=" ")
            j -= 1
            visited_elems += 1
        left = left + 1
    print("")


if __name__ == "__main__":
    print_matrix_spirally([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3, 3)
    print_matrix_spirally([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], 4, 4)
    print_matrix_spirally([[1,2,3],[4,5,6],[7,8,9],[10,11,12]], 4, 3)
    print_matrix_spirally([[1,2,3,4],[5,6,7,8],[9,10,11,12]], 3, 4)
