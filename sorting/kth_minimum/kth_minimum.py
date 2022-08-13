def kth_minimum(arr, k):
    if k > len(arr):
        print(-1)
        return

    for i in range(0, k):
        current_min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[current_min_idx]:
                current_min_idx = j
        arr[i], arr[current_min_idx] = arr[current_min_idx], arr[i]

    print(arr[k - 1])


if __name__ == "__main__":
    kth_minimum([2, 0, 5, 7, 3, 8, 4, 1], 2)
    kth_minimum([2, 0, 5, 7, 3, 8, 4, 1], 5)
    kth_minimum([2, 0, 5, 7, 3, 8, 4, 1], 10)
