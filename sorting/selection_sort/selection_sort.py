def selection_sort(arr):
    result = list()

    for i in range(0, len(arr) - 1):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j

        result.append(min_idx)
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    print(result)


if __name__ == "__main__":
    selection_sort([6, 4, 3, 7, 2, 8])
