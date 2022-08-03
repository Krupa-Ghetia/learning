import functools
import math


def pascal_triangle(num):

    result = []
    for i in range(0, num):
        result.append([])

        for j in range(0, num):
            if j > i:
                result[-1].append(0)
            else:
                result[-1].append(math.floor(find_combination(i, j)))

    print(result)


def find_combination(n, r):

    if r == 0 or r == n or n == 0:
        return 1

    num_list = list(range(1, n+1))
    numerator = functools.reduce(lambda x, y: x * y, num_list)
    denominator_1 = functools.reduce(lambda x, y: x * y, num_list[:n-r])
    denominator_2 = functools.reduce(lambda x, y: x * y, num_list[:r])

    return numerator / (denominator_1 * denominator_2)


if __name__ == "__main__":
    pascal_triangle(5)
