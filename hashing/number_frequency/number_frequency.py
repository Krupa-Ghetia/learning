def number_frequency(arr):
    freq = dict()
    for i in arr:
        count = freq.get(i, 0)
        freq[i] = count + 1

    print(freq)


if __name__ == "__main__":
    number_frequency([1, 2, 3, 6, 2, 4, 1, 5, 7, 6, 1])
