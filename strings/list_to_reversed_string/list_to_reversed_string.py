def list_to_reversed_string(arr):
    reversed_string = str()

    for x in arr:
        reversed_string = x + reversed_string

    print(reversed_string)


if __name__ == "__main__":
    list_to_reversed_string(['s', 'c', 'a', 'l', 'e', 'r'])
