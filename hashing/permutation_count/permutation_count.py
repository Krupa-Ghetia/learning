def permutation_count(substr, str):
    substr_hash = dict()
    str_hash = dict()
    substring_count = 0

    for i in range(0, len(substr)):
        substr_hash[substr[i]] = substr_hash.get(substr[i], 0) + 1
        str_hash[str[i]] = str_hash.get(str[i], 0) + 1

    for i in range(len(substr), len(str)):
        substring_count += compare_hash(str_hash, substr_hash)

        str_hash[str[i - len(substr)]] -= 1
        str_hash[str[i]] = str_hash.get(str[i], 0) + 1

    substring_count += compare_hash(str_hash, substr_hash)

    print(substring_count)


def compare_hash(str_hash, substr_hash):

    for k in substr_hash.keys():
        if k not in str_hash.keys():
            return 0
        if str_hash[k] != substr_hash[k]:
            return 0
    return 1


if __name__ == "__main__":
    permutation_count('abc', 'abcbacabc')
    permutation_count('docp', 'aoapeooeoapcpaocecddoocdcqqapeapccc')