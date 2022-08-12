def verify_AP(arr):
    diff = abs(arr[0] - arr[1])
    first_elem = min(arr)
    elem_hash = dict()

    for el in arr:
        elem_hash[el] = 0

    for i in range(0, len(arr) - 1):
        if (first_elem + (i * diff)) not in elem_hash:
            print(False)
            return
    print(True)


if __name__ == "__main__":
    verify_AP([3, 1, 5])
    verify_AP([3, 5, 2, 8])
