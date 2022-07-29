def rotate_array(arr, k):
    arr_len = len(arr)
    pos_arr = []

    for i in range(0, arr_len):
        shift_pos = (i + k) % arr_len
        pos_arr.append((shift_pos, arr[i]))

    for x in pos_arr:
        arr[x[0]] = x[1]

    print(arr)


if __name__ == "__main__":
    rotate_array([1, 2, 3, 4, 5, 6, 7], 3)
    rotate_array([1, 2, 3, 4, 5, 6, 7], 1)
    rotate_array([1, 2, 3, 4], 2)
    rotate_array([1, 2, 3], 5)
