def fill_matrix_spirally(size):
    curr_elem = 1
    top = 0
    bottom = size - 1
    left = 0
    right = size - 1

    mat = generate_empty_matrix(size)

    while curr_elem <= size * size:

        for j in range(left, right + 1):
            mat[top][j] = curr_elem
            curr_elem += 1
        top += 1

        for j in range(top, bottom + 1):
            mat[j][right] = curr_elem
            curr_elem += 1
        right -= 1

        for j in range(right, left - 1, -1):
            mat[bottom][j] = curr_elem
            curr_elem += 1
        bottom -= 1

        for j in range(bottom, top - 1, -1):
            mat[j][left] = curr_elem
            curr_elem += 1
        left += 1

    print(mat)


def generate_empty_matrix(size):

    mat = []
    for i in range(0, size):
        mat.append([])
        for j in range(0, size):
            mat[i].append(0)

    return mat


if __name__ == "__main__":
    fill_matrix_spirally(5)
    fill_matrix_spirally(4)
    fill_matrix_spirally(2)
