def get_array_rotations(arr, rot):
    result = []

    for k in rot:
        result.append(rotate_array(arr[:], k))

    print(result)


def rotate_array(arr, k):
    arr_len = len(arr)
    mod = k % arr_len
    pos_arr = []

    for i in range(0, arr_len):
        pos_arr.append((i, arr[(mod + i) % arr_len]))

    for x in pos_arr:
        arr[x[0]] = x[1]

    return arr


if __name__ == "__main__":
    get_array_rotations([1, 2, 3, 4, 5], [2, 3])
