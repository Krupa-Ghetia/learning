def odd_elem_subarray(arr, k):
    prefix_hash = dict()
    count = 0

    odd_elem_count = 0

    for i in range(0, len(arr)):

        if arr[i] % 2 != 0:
            odd_elem_count += 1

        if odd_elem_count == k:
            count += 1

        if (odd_elem_count - k) in prefix_hash:
            count += prefix_hash.get(odd_elem_count - k)

        hash_value = prefix_hash.get(odd_elem_count, 0)
        prefix_hash[odd_elem_count] = hash_value + 1

    print(count)


if __name__ == "__main__":
    odd_elem_subarray([2, 4, 1, 3, 8], 1)
    odd_elem_subarray([2, 4, 1, 8, 3], 1)
