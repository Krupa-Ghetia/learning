def clear_array(arr):
    arr.sort()

    for i in range(len(arr) - 1, -1, -1):
        arr.pop(i)

    print(arr)


if __name__ == "__main__":
    clear_array([2, 3, 1, 4, 7, 6, 5])
