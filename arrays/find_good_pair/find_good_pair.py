def check_good_pair(arr, k):
    for i in range(0, len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == k:
                print(1)
                return
    print(0)


if __name__ == "__main__":
    check_good_pair([1, 2, 3, 4], 7)
    check_good_pair([1, 2, 4], 4)
    check_good_pair([1, 2, 2], 4)
