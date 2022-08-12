def count_sort(arr):
    count_0 = 0
    count_1 = 0
    count_2 = 0

    for el in arr:
        if el == 0:
            count_0 += 1
        elif el == 1:
            count_1 += 1
        else:
            count_2 += 1

    sorted_list = [0] * count_0 + [1] * count_1 + [2] *count_2

    print(sorted_list)


if __name__ == "__main__":
    count_sort([1, 0, 1, 2, 1, 0, 1, 2, 2])
