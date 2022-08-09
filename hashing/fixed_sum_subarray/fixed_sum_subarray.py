def fixed_sum_subarray(arr, k):
    prefix_hash = dict()
    prefix_sum = 0
    start_idx = len(arr)
    end_idx = len(arr)

    for i in range(0, len(arr)):
        prefix_sum += arr[i]
        if prefix_sum == k:
            start_idx, end_idx = 0, i
            break
        elif (prefix_sum - k) in prefix_hash:
            hash_value = prefix_hash.get(prefix_sum - k)
            if hash_value + 1 < start_idx:
                start_idx, end_idx = hash_value + 1, i
        else:
            prefix_hash[prefix_sum] = i

    if start_idx < len(arr):
        print(arr[start_idx: end_idx + 1])
    else:
        print([-1])


if __name__ == "__main__":
    fixed_sum_subarray([1, 2, 3, 4, 5], 5)
    fixed_sum_subarray([5, 10, 20, 100, 105], 110)
