import random


def strictly_smaller_greater(integer_list):
    integer_list_length = len(integer_list)
    integer_list.sort()
    first_elem_count = integer_list.count(integer_list[0])
    last_elem_count = integer_list.count(integer_list[-1])

    if integer_list_length <= 2:
        print(f"Count of integers having strictly smaller and greater element is 0")

    elif integer_list_length == first_elem_count:
        print(f"Count of integers having strictly smaller and greater element is 0")
    else:
        print(f"Count of integers having strictly smaller and greater element is "
              f"{integer_list_length - first_elem_count - last_elem_count}")


if __name__ == "__main__":
    strictly_smaller_greater(random.sample(range(0, 1000), 50))
    strictly_smaller_greater(random.sample(range(0, 500), 25))
    strictly_smaller_greater(random.sample(range(0, 700), 40))
    strictly_smaller_greater([543])
    strictly_smaller_greater([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
    strictly_smaller_greater([5, 5])
    strictly_smaller_greater([3, 247, 3, 45, 7, 247, 25, 14, 3, 97, 135, 200, 9, 78, 97])


