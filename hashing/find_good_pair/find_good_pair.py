def find_good_pair(arr, k):
    array_map = dict()
    for x in arr:
        if array_map.get(k - x, 0):
            print(True)
            return
        array_map[x] = 1

    print(False)


if __name__ == "__main__":
    find_good_pair([1, 2, 3, 4], 7)
    find_good_pair([1, 2, 4], 4)
    find_good_pair([1, 2, 2], 4)
