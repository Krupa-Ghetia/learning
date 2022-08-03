def generate_matrix(size):
    result = get_empty_matrix(size)

    for i in range(0, size):
        col = size - 1
        for val in range(1, i+2):
            result[i][col] = val
            col -= 1

    print(result)


def get_empty_matrix(size):
    mat = []
    for i in range(0, size):
        mat.append([])
        for j in range(0, size):
            mat[i].append(0)

    return mat


if __name__ == "__main__":
    generate_matrix(3)


