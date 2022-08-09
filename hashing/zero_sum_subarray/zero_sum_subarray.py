def zero_sum_subarray(A):
    prefix_hash = dict()
    prefix_sum = 0

    for i in range(0, len(A)):
        prefix_sum += A[i]
        if prefix_sum == 0 or prefix_hash.get(prefix_sum):
            print(1)
            return
        else:
            prefix_hash[prefix_sum] = i

    print(0)


if __name__ == "__main__":
    zero_sum_subarray([1, 2, 3, 4, 5])
    zero_sum_subarray([-1, 1])
    zero_sum_subarray([7, 1, 3, -1, 4, -1, 0, -1, 18])
