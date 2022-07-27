import math


def reverse_the_array(arr):
    arr_len = len(arr)
    for i in range(0, math.floor(arr_len / 2)):
        arr[i], arr[arr_len - 1 - i] = arr[arr_len - 1 - i], arr[i]

    print(arr)


if __name__ == "__main__":
    reverse_the_array([1, 2, 3, 4])
    reverse_the_array([True, False])
    reverse_the_array(['abc', 'xyz', 'pqr'])
    reverse_the_array([3, 5, 7, 4, 2, 1, 9, 7, 0, 6])
    reverse_the_array(['hello'])
