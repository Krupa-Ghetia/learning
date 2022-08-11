def colourful_number(A):
    number_list = [int(x) for x in str(A)]
    product_hash = dict()

    for i in range(0, len(number_list)):

        if product_hash.get(number_list[i]):
            print(0)
            return
        product_hash[number_list[i]] = 1

        product = number_list[i]
        for j in range(i + 1, len(number_list)):
            product *= number_list[j]

            if product_hash.get(product):
                print(0)
                return
            product_hash[product] = 1
    print(1)


if __name__ == "__main__":
    colourful_number(3245)
    colourful_number(23)
    colourful_number(236)