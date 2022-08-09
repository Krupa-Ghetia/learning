def sum_pairs(arr):
    sum_pair_hash = dict()
    result = []

    for i in range(0, len(arr) - 1):
        for j in range(i + 1, len(arr)):
            hash_value = sum_pair_hash.get(arr[i] + arr[j])
            if not hash_value:
                sum_pair_hash[arr[i] + arr[j]] = (i, j)
                continue

            if i not in hash_value and j not in hash_value:
                if not len(result):
                    result = [hash_value[0], hash_value[1], i, j]
                elif (hash_value[0] < result[0]) or \
                     (hash_value[0] == result[0] and hash_value[1] < result[1]) or \
                     (hash_value[0] == result[0] and hash_value[1] == result[1] and i < result[2]) or \
                     (hash_value[0] == result[0] and hash_value[1] == result[1] and i == result[2] and j < result[3]):

                    result = [hash_value[0], hash_value[1], i, j]
    print(result)


if __name__ == "__main__":
    sum_pairs([3, 4, 7, 1, 2, 9, 8])
    sum_pairs([3, 7, 7, 1])
    sum_pairs([2, 5, 1, 6])
    sum_pairs([1, 1, 1, 1, 1])
