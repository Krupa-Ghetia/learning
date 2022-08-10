def is_dictionary(arr, order):
    alphabet_hash = dict()
    for i in range(0, len(order)):
        alphabet_hash[order[i]] = i

    for i in range(0, len(arr) - 1):
        word_1 = arr[i]
        word_2 = arr[i + 1]
        min_len = min(len(word_1), len(word_2))

        for j in range(0, min_len):
            if alphabet_hash.get(word_1[j]) > alphabet_hash.get(word_2[j]):
                print(0)
                return

            if alphabet_hash.get(word_1[j]) < alphabet_hash.get(word_2[j]):
                break

            if alphabet_hash.get(word_1[j]) == alphabet_hash.get(word_2[j]):
                if j == (min_len - 1) and (len(word_2) < len(word_1)):
                    print(0)
                    return
    print(1)


if __name__ == "__main__":
    is_dictionary(["hello", "scaler", "interviewbit"], "adhbcfegskjlponmirqtxwuvzy")
    is_dictionary(["fine", "none", "no"], "qwertyuiopasdfghjklzxcvbnm")
