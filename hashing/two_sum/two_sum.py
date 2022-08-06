def two_sum(arr, k):
    array_map = dict()
    for i in range(len(arr)):
        if array_map.get(k - arr[i]):
            print([array_map.get(k - arr[i]), i + 1])
            return
        if not array_map.get(arr[i]):
            array_map[arr[i]] = i + 1
    print([])


if __name__ == "__main__":
    two_sum([ -5, 1, 4, -7, 10, -7, 0, 7, 3, 0, -2, -5, -3, -6, 4, -7, -8, 0, 4, 9, 4, 1, -8, -6, -6, 0, -9, 5, 3, -9, -5, -9, 6, 3, 8, -10, 1, -2, 2, 1, -9, 2, -3, 9, 9, -10, 0, -9, -2, 7, 0, -4, -3, 1, 6, -3 ], -1)