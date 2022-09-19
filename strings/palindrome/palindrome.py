def palindrome(input_str):
    left = 0
    right = len(input_str) - 1

    while left < right:
        if input_str[left] != input_str[right]:
            print('Not Palindrome')
            return
        left += 1
        right -= 1

    print('Palindrome')


if __name__ == "__main__":
    palindrome('malayalam')
    palindrome('dfbigfh')
    palindrome('aabcdaa')