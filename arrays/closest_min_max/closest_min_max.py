def closest_min_max(arr):
    min_value, max_value = get_min_max_values(arr)
    min_idx = -1
    max_idx = -1
    min_size = len(arr)

    for i in range(len(arr)-1, -1, -1):
        if arr[i] == min_value:
            min_idx = i
            if max_idx != -1:
                min_size = min(min_size, abs(min_idx-max_idx)+1)

        if arr[i] == max_value:
            max_idx = i
            if min_idx != -1:
                min_size = min(min_size, abs(min_idx-max_idx)+1)

    print(min_size)


def get_min_max_values(arr):

    min_value = arr[0]
    max_value = arr[1]

    for i in range(0, len(arr)):
        if arr[i] < min_value:
            min_value = arr[i]
        if arr[i] > max_value:
            max_value = arr[i]

    return min_value, max_value


if __name__ == "__main__":
    closest_min_max([1, 2, 3, 1, 3, 4, 4])
