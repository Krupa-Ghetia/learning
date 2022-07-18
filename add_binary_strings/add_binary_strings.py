def add_binary_strings(A, B):
    max_len = max(len(A), len(B))
    A = A.zfill(max_len)
    B = B.zfill(max_len)
    carry = 0
    result = ""

    for i in range(max_len - 1, -1, -1):
        if A[i] != B[i] and carry == 0:
            result = "1" + result
        elif A[i] != B[i] and carry == 1:
            result = "0" + result
        elif A[i] == "0":
            result = f"{carry}{result}"
            carry = 0
        elif A[i] == "1":
            result = f"{carry}{result}"
            carry = 1

    if carry == 1:
        result = "1" + result

    print(result)


if __name__ == "__main__":
    add_binary_strings("1110", "110")
