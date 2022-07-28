def fizzBuzz(num):
    result = []
    for i in range(1, num + 1):
        print(i, i % 3, i % 5)
        if (i % 3 == 0) & (i % 5 == 0):
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append("{}".format(i))

    print(result)


if __name__ == "__main__":
    fizzBuzz(3)
