def array_intersection(arr1, arr2):
    array_map = dict()
    for x in arr1:
        count = array_map.get(x, 0)
        array_map[x] = count + 1

    intersection = list()
    for x in arr2:
        if array_map.get(x, 0):
            array_map[x] -= 1
            intersection.append(x)

    print(intersection)


if __name__ == "__main__":
    array_intersection([1, 2, 3, 5, 4, 6, 8, 3], [2, 7, 9, 3, 3, 3])
