def add_one_to_number(arr):
    arr = [str(x) for x in arr]
    digit = str(int("".join(arr)) + 1)
    print(" ".join(digit.split()))


if __name__ == "__main__":
    add_one_to_number([1, 2, 3])
    add_one_to_number([1, 2, 9])
