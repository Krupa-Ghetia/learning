import math


def reverse_the_array(arr, start_idx, end_idx):
    subarr_len = end_idx - start_idx
    for i in range(start_idx, start_idx + math.floor((subarr_len + 1) / 2)):
        arr[i], arr[(start_idx + subarr_len) - (i - start_idx)] = arr[(start_idx + subarr_len) - (i - start_idx)], arr[i]

    print(arr)


if __name__ == "__main__":
    reverse_the_array([1, 2, 3, 4, 5, 6, 7, 8, 9], 2, 6)
    reverse_the_array(['abc', 'xyz', 'pqr', 'lmn', 'jkl'], 1, 2)
    reverse_the_array(['hello'], 0, 0)
