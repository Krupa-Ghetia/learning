def search_sorted_matrix(A, B):
    result = -1

    for i in range(0, len(A)):
        if A[i][0] > B or A[i][-1] < B:
            continue

        for j in range(0, len(A[i])):
            if A[i][j] == B and result == -1:
                result = (i + 1) * 1009 + (j + 1)

    print(result)


if __name__ == "__main__":
    search_sorted_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 5)
    search_sorted_matrix([[1, 3, 5], [2, 4, 6], [3, 5, 7]], 5)
