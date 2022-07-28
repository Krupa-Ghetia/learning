def get_time_to_equality(arr):
    max_elem = max(arr)
    min_time = 0

    for x in arr:
        min_time += max_elem - x

    print(min_time)


if __name__ == "__main__":
    get_time_to_equality([2, 4, 1, 3, 2])
