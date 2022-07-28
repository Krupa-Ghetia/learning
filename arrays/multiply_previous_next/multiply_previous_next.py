def multiply_previous_next(arr):
    previous_elem = None

    if len(arr) == 1:
        print(arr)
        return

    for i in range(0, len(arr)):
        if i == 0:
            previous_elem = arr[i]
            arr[i] = arr[i] * arr[i + 1]
        elif i == len(arr) - 1:
            arr[i] = arr[i] * previous_elem
        else:
            current_elem = arr[i]
            arr[i] = previous_elem * arr[i + 1]
            previous_elem = current_elem

    print(arr)


if __name__ == "__main__":
    multiply_previous_next([1, 2, 3, 4, 5])
    multiply_previous_next([5, 17, 100, 11])
    multiply_previous_next([0])
