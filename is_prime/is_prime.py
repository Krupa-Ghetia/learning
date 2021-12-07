def is_prime(number):
    i = 2
    number_is_prime = True

    while i*i < number:
        if number % i == 0:
            number_is_prime = False
            break
        i += 1

    if number_is_prime:
        print(f"{number} is prime.")
    else:
        print(f"{number} is not prime.")


if __name__ == "__main__":
    is_prime(5)
    is_prime(100)
    is_prime(1024)
    is_prime(11)
    is_prime(21)
    is_prime(81)
    is_prime(3)