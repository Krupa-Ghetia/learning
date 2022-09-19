def reverse_sentence(sentence):
    result = str()
    start = 0

    for i in range(len(sentence)):

        if sentence[i] == ' ':
            result = sentence[start: i + 1] + result
            start = i + 1

    result = sentence[start:] + ' ' + result
    result = result.strip()

    print(result)


if __name__ == "__main__":
    reverse_sentence('Today is Monday')
