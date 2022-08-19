def wave_array(arr):
    arr.sort()

    for i in range(0, len(arr) - 1, 2):
        arr[i], arr[i + 1] = arr[i + 1], arr[i]

    print(arr)


if __name__ == "__main__":
    wave_array([1, 2, 3, 4])
    wave_array([1, 2])
