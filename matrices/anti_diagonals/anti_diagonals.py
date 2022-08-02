def anti_diagonals(mat):
    max_idx = len(mat) - 1
    start = 0
    end = 0
    result = []

    while start <= max_idx:
        i = start
        j = end

        result.append([])
        while i <= end:
            result[-1].append(mat[i][j])
            i += 1
            j -= 1

        if end == max_idx:
            start += 1
        else:
            end += 1

    result = fill_zeros(result, max_idx)
    print(result)


def fill_zeros(mat, max_idx):
    for i in range(0, (max_idx * 2) + 1):
        for j in range(len(mat[i]), max_idx + 1):
            mat[i].append(0)

    return mat


if __name__ == "__main__":
    anti_diagonals([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
    anti_diagonals([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    anti_diagonals([[1, 2], [3, 4]])
