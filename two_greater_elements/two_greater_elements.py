def two_greater_elements(interger_list):
    for elem_count in range(2):
        largest_elem = max(interger_list)
        interger_list = [x for x in interger_list if x != largest_elem]

    print(interger_list)


if __name__ == "__main__":
    two_greater_elements([-2, -99, 0, 5, 1, 76, 0, -5, 1, 63, 39, 25])
