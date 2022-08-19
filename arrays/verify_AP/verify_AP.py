def verify_AP(arr):
    first_elem = min(arr)
    second_elem = max(arr)
    elem_hash = dict()

    for el in arr:
        if first_elem < el < second_elem:
            second_elem = el

        elem_hash[el] = 0

    diff = abs(first_elem - second_elem)

    for i in range(0, len(arr)):
        if (first_elem + (i * diff)) not in elem_hash:
            print(False)
            return
    print(True)


if __name__ == "__main__":
    verify_AP([3, 1, 5])
    verify_AP([3, 5, 2, 8])
    verify_AP([2, 4, 1])
    verify_AP([-39, -39])
