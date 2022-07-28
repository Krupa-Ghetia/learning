def get_odd_even_subsequence_len(arr):
    temp_elem = None
    result = []

    for i in range(0, len(arr)):
        if i == 0:
            result.append(arr[i])
            temp_elem = arr[i]
            continue

        if arr[i] % 2 == temp_elem % 2:
            continue

        result.append(arr[i])
        temp_elem = arr[i]

    print(len(result))


if __name__ == "__main__":
    get_odd_even_subsequence_len([1, 2, 2, 5, 6])
    get_odd_even_subsequence_len([2, 2, 2, 2, 2, 2])
