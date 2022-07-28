def get_primal_power(arr):
    primal_power = 0

    for x in arr:
        if x <= 1:
            continue
        else:
            primal_power += is_prime(x)

    print(primal_power)


def is_prime(num):
    if num == 2:
        return 1

    i = 2
    while i * i <= num:
        if num % i == 0:
            return 0
        i += 1
    return 1


if __name__ == "__main__":
    get_primal_power([-6, 10, 12])
    get_primal_power([-11, 7, 8, 9, 10, 11])
