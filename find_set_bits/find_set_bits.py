def find_set_bits(numbers):
    total = 0
    shift_count = 0
    set_bits = []

    for num in numbers:
        total += 1 << num

    print(total)

    while total != 0:
        if total & 1 == 1:
            set_bits.append(shift_count)

        total = total >> 1
        shift_count += 1

    print(set_bits)


if __name__ == "__main__":
    find_set_bits([1, 2, 1])
    find_set_bits([1, 2, 3])