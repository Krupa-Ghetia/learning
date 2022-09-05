import sys


def minimize_difference(arr, k):
    min_elem = sys.maxsize
    max_elem = -sys.maxsize - 1
    freq_hash = dict()

    for x in arr:
        min_elem = min(min_elem, x)
        max_elem = max(max_elem, x)
        freq_hash[x] = freq_hash.get(x, 0) + 1

    while min_elem < max_elem and k > 0:
        min_count = freq_hash.get(min_elem)
        max_count = freq_hash.get(max_elem)

        if min_count <= max_count:
            if min_count > k:
                break

            freq_hash[min_elem + 1] = freq_hash.get(min_elem + 1, 0) + min_count
            k -= min_count
            freq_hash[min_elem] = 0
            min_elem += 1

        elif max_count < min_count:
            if max_count > k:
                break

            freq_hash[max_elem - 1] = freq_hash.get(max_elem - 1, 0) + max_count
            k -= max_count
            freq_hash[max_elem] = 0
            max_elem -= 1

    print(max_elem - min_elem)


if __name__ == "__main__":
    minimize_difference([2, 6, 3, 9, 8], 3)
    minimize_difference([4, 6, 3, 1, 4], 5)
