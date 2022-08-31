def element_removal(arr):
    cost = 0
    sum_of_arr = sum(arr)
    arr.sort()

    start_idx = len(arr) - 1
    for i in range(start_idx, -1, -1):
        cost += sum_of_arr
        sum_of_arr -= arr.pop(i)

    print(cost)


if __name__ == "__main__":
    element_removal([2, 1, 3, 6, 4, 5])
    element_removal([5])
    element_removal([])
