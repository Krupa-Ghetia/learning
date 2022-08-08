def validate_sudoku(A):
    for i in range(0, 9):
        row = {}
        column = {}
        block = {}
        row_cube = 3 * (i // 3)
        col_cube = 3 * (i % 3)
        for j in range(0, 9):
            if A[i][j] != '.' and A[i][j] in row:
                print(0)
                return
            row[A[i][j]] = 1

            if A[j][i] != '.' and A[j][i] in column:
                print(0)
                return
            column[A[j][i]] = 1

            row_idx = row_cube + (j // 3)
            col_idx = col_cube + (j % 3)
            if A[row_idx][col_idx] != '.' and A[row_idx][col_idx] in block:
                print(0)
                return
            block[A[row_idx][col_idx]] = 1

    print(1)


if __name__ == "__main__":
    validate_sudoku(["53..7....", "6..195...", ".98....6.", "8...6...3", "4..8.3..1", "7...2...6", ".6....28.", "...419..5", "....8..79"])