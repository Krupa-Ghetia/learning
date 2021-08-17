# Given a number n check if it is a perfect square
def square_root(num):
    start = 0
    end = num

    while start <= end:

        mid = (start + end) >> 1

        if mid * mid == num:
            return f"""{num} is a perfect square."""

        if mid * mid > num:
            end = mid - 1

        if mid * mid < num:
            start = mid + 1

    return f"""{num} is not a perfect square."""


if __name__ == "__main__":
    status = square_root(100)
    print(status)
