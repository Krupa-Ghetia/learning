def possible_palindrome(input_str):
    left = 0
    right = len(input_str) - 1
    mismatch = 0

    while left < right:
        if input_str[left] != input_str[right]:
            mismatch += 1

        left += 1
        right -= 1

    if mismatch == 1 or (mismatch == 0 and len(input_str) % 2 != 0):
        print("Possible Palindrome")
    else:
        print("Not a possible Palindrome")


if __name__ == "__main__":
    possible_palindrome("abccba")
    possible_palindrome("abcba")
    possible_palindrome("abccda")
