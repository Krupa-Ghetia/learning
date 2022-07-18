def find_the_missing_cow(cows):
    total_cows = len(cows) + 1
    result = 0

    for num in range(total_cows + 1):
        result = result ^ num

    for cow in cows:
        result = result ^ cow

    print(f"Cow with number {result} is missing,")


if __name__ == "__main__":
    find_the_missing_cow([2, 3, 4, 1, 6])
    find_the_missing_cow([4, 2, 3, 1, 5, 9, 6, 7])
