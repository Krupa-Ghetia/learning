def largest_number(A):
    str_array = list()

    for i in range(0, len(A)):
        str_array.append(str(A[i]))

    for i in range(0, len(str_array)):
        for j in range(i + 1, len(str_array)):
            if str_array[j] + str_array[i] > str_array[i] + str_array[j]:
                str_array[i], str_array[j] = str_array[j], str_array[i]

    result = ''.join(str_array)

    if result == '0'*len(result):
        print(0)
    else:
        print(result)


if __name__ == "__main__":
    largest_number([3, 30, 34, 5, 9, 93])
    largest_number([2, 3, 9, 0])
    largest_number([0, 0, 0, 0, 0])
