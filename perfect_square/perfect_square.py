import math


def square_root(number):
    start = 1
    end = number

    while start < end:
        mid = math.floor((start + end) / 2)

        if mid * mid == number:
            print(f"{number} is a perfect square. Square root of {number} is {mid}.")
            return
        elif mid * mid > number:
            end = mid - 1
        elif mid * mid < number:
            start = mid + 1
    print(f"{number} is not a perfect square.")


if __name__ == "__main__":
    square_root(16)
    square_root(34)
    square_root(100)
    square_root(256)
    square_root(578)
    square_root(1000)