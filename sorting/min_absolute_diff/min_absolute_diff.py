def min_absolute_diff(arr):
    min_diff = max(arr)
    min_diff_pairs = list()
    arr.sort()

    for i in range(0, len(arr) - 1):
        current_diff = arr[i + 1] - arr[i]
        if current_diff == min_diff and (arr[i], arr[i + 1]) not in min_diff_pairs:
            min_diff_pairs.append((arr[i], arr[i + 1]))

        elif current_diff < min_diff:
            min_diff = arr[i + 1] - arr[i]
            min_diff_pairs.clear()
            min_diff_pairs.append((arr[i], arr[i + 1]))

    print(min_diff_pairs)


if __name__ == "__main__":
    min_absolute_diff([3, 2, 1, 4, 6])
    min_absolute_diff([2, 3, 4, 6, 3, 3, 1])
