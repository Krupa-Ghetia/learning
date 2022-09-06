def reverse_string(input_str):
    result = str()

    for x in input_str:
        result = x + result

    print(result)


if __name__ == "__main__":
    reverse_string('scaler')