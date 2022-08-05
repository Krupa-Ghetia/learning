def longest_contigeous_substring(input_str):
    left = []
    right = []
    max_len = 0
    total_ones = 0

    cons_count = 0
    for val in input_str:
        if val == '1':
            cons_count += 1
            total_ones += 1
            left.append(cons_count)
        else:
            cons_count = 0
            left.append(cons_count)

    cons_count = 0
    for val in input_str[::-1]:
        if val == '1':
            cons_count += 1
            right.insert(0, cons_count)
        else:
            cons_count = 0
            right.insert(0, cons_count)

    for i in range(0, len(input_str)-1):
        if i == 0:
            if input_str[i] == '1':
                max_len = max(max_len, (left[i] + right[i] - 1))
            elif (right[i + 1] + 1) <= total_ones:
                max_len = max(max_len, (right[i + 1] + 1))
            else:
                max_len = max(max_len, (right[i + 1]))
        else:
            if input_str[i] == '1':
                max_len = max(max_len, (left[i] + right[i] - 1))
            elif (left[i-1] + right[i+1] + 1) <= total_ones:
                max_len = max(max_len, (left[i-1] + right[i+1] + 1))
            else:
                max_len = max(max_len, (left[i-1] + right[i+1]))

    print(max_len)


if __name__ == "__main__":
    longest_contigeous_substring("111011101")
    longest_contigeous_substring("1111011110")
    longest_contigeous_substring("11111")
    longest_contigeous_substring("011110001001")
