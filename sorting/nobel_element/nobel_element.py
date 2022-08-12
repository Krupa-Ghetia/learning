def nobel_element(arr):
    # Sort the array
    arr.sort()

    for i in range(0, len(arr)):
        if i + 1 == len(arr) or arr[i] == arr[i + 1]:
            continue

        if arr[i] == len(arr) - i - 1:
            print(arr[i])
            return

    print(-1)


if __name__ == "__main__":
    nobel_element([3, 2, 1, 4])
    nobel_element([1, 2, 3, 4, 5])
    nobel_element([1, 2, 4, 4, 6, 8, 10])
