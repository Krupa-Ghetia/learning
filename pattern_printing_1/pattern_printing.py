def pattern_printing(num):
    result = []

    for i in range(0, num):
        temp = []
        for j in range(0, num):
            if j == i:
                temp.append(i + 1)
            elif j > i:
                temp.append(0)
            else:
                temp.append(i + 1 - (i - j))
        result.append(temp)

    print(result)


if __name__ == "__main__":
    pattern_printing(3)
    pattern_printing(4)