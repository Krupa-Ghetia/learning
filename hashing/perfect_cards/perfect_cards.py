def perfect_cards(A):
    card_hash = dict()

    for i in range(0, len(A)):
        hash_value = card_hash.get(A[i], 0)
        card_hash[A[i]] = hash_value + 1

    keys = list(card_hash.keys())
    if len(keys) > 2:
        print("LOSE")
    elif card_hash.get(keys[0]) != card_hash.get(keys[1]):
        print("LOSE")
    else:
        print("WIN")


if __name__ == "__main__":
    perfect_cards([1, 1, 2, 2, 2])
    perfect_cards([1, 2])
    perfect_cards([1, 1, 2, 2, 3])
