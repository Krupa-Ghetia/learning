def xor_pairs(arr, k):
    array_map = dict()
    result = set()
    for x in arr:
        if array_map.get(k ^ x):
            if x < k ^ x:
                result.add((x, k ^ x))
            else:
                result.add((k ^ x, x))

            array_map[k ^ x] -= 1
        else:
            array_map[x] = array_map.get(x, 0) + 1

    print(len(result))


if __name__ == "__main__":
    xor_pairs([5, 4, 10, 15, 7, 6], 5)
    xor_pairs([3, 6, 8, 10, 15, 50], 5)
