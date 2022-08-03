def special_subsequence(seq):
    count_of_ag = 0
    count_of_g = 0

    for i in range(len(seq) - 1, -1, -1):
        if seq[i] == 'g':
            count_of_g += 1
        if seq[i] == 'a':
            count_of_ag += count_of_g

    print(count_of_ag)


if __name__ == "__main__":
    special_subsequence('abcgag')
    special_subsequence('aggbcdaggac')
