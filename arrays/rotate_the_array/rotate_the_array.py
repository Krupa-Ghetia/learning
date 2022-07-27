def rotate_array(arr, k):
    if k >= len(arr):
        print("Rotation steps should be less than array length")
        return

    arr_len = len(arr)
    temp_subarr = arr[arr_len - k: arr_len]
    subarray_idx = k - 1

    for i in range(arr_len - 1, -1, -1):
        elem_idx_to_move = i - k

        if elem_idx_to_move < 0:
            arr[i] = temp_subarr[subarray_idx]
            subarray_idx -= 1
            continue

        arr[i] = arr[elem_idx_to_move]

    print(arr)


if __name__ == "__main__":
    rotate_array([1, 2, 3, 4, 5, 6, 7], 3)
    rotate_array([1, 2, 3, 4, 5, 6, 7], 1)
    rotate_array([1, 2, 3, 4], 4)
    rotate_array([1, 2, 3], 5)
