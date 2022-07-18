def find_the_bachelor(numbers):
    result = 0

    for numb in numbers:
        result = result ^ numb

    print(f"{result} is a bachelor.")


if __name__ == "__main__":
    find_the_bachelor([1, 4, 2, 1, 5, 3, 2, 5, 4])
    find_the_bachelor([9, 24, 17, 24, 9])
