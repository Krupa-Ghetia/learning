def min_max_picks(integer_list):
    max_even = None
    min_odd = None
    integer_list.sort()

    for i in range(len(integer_list) - 1, -1, -1):
        if integer_list[i] % 2 == 0:
            max_even = integer_list[i]
            break

    for i in range(0, len(integer_list) - 1):
        if integer_list[i] % 2 != 0:
            min_odd = integer_list[i]
            break

    print(max_even - min_odd)


if __name__ == "__main__":
    min_max_picks([-98, 54, -52, 15, 23, -97, 12, -64, 52, 85])
