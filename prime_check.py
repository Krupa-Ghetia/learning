# Check whether a given number is prime or not

import math


def is_prime(number):

    if number <= 1:
        print(f"""{number} is not prime""")
        return

    for i in range(2, int(math.sqrt(number)) + 1):

        if number % i == 0:
            print(f"""{number} is not prime.""")
            return

    print(f"""{number} is prime""")


if __name__ == "__main__":
    is_prime(2)
    is_prime(5)
    is_prime(7)
    is_prime(11)
    is_prime(199)
    is_prime(4)
    is_prime(16)
    is_prime(50)
    is_prime(75)
    is_prime(0)
    is_prime(1)
    is_prime(-11)
