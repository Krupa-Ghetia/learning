def array_intersection(arr1, arr2):
    arr1_map = dict()
    for x in arr1:
        arr1_map[x] = 1

    intersection = set()
    for x in arr2:
        if arr1_map.get(x, 0):
            intersection.add(x)

    print(intersection)


if __name__ == "__main__":
    array_intersection([1, 2, 3, 5, 4, 6, 8], [2, 7, 9, 3, 3])
