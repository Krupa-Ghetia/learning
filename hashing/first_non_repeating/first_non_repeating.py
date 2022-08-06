def first_non_repeating(arr):
    freq = dict()
    for x in arr:
        count = freq.get(x, 0)
        freq[x] = count + 1

    for x in arr:
        if freq[x] == 1:
            print(x)
            return


if __name__ == "__main__":
    first_non_repeating([1, 2, 3, 6, 2, 4, 1, 5, 7, 6, 1])
