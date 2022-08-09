def sum_pairs(arr):
    sum_pair_hash = dict()

    for i in range(0, len(arr) - 1):
        for j in range(i + 1, len(arr)):
            hash_value = sum_pair_hash.get(arr[i] + arr[j])
            if hash_value:
                if hash_value[0] != i and hash_value[0] != j and hash_value[1] != i and hash_value[1] != j:
                    print(True)
                    return
            else:
                sum_pair_hash[arr[i] + arr[j]] = (i, j)
    print(False)


if __name__ == "__main__":
    sum_pairs([3, 4, 7, 1, 2, 9, 8])
    sum_pairs([3, 7, 7, 1])
