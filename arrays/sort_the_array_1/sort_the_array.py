def sort_the_array(arr):
    element_to_move = arr[len(arr) - 1]

    for i in range(len(arr) - 2, -1, -1):
        if i == 0:
            if element_to_move < arr[i]:
                arr[i+1] = arr[i]
                arr[i] = element_to_move
            else:
                arr[i + 1] = element_to_move
        elif element_to_move < arr[i]:
            arr[i + 1] = arr[i]
        elif element_to_move > arr[i]:
            arr[i + 1] = element_to_move
            break

    print(arr)


if __name__ == "__main__":
    sort_the_array([1, 2, 3, 6, 8, 15, 20, 14])
    sort_the_array([3, 5, 7, 8, 9, 12, 15, 16, 19, 25, 30, 1])
    sort_the_array([1, 3, 6, 8, 15, 20, 2])
