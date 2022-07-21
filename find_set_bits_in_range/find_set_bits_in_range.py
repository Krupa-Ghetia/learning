import math


class Solution:
    # @param A : integer
    # @return an integer
    @classmethod
    def solve(cls, number):
        total_set_bits = 0

        for i in range(1, number + 1):
            total_set_bits += Solution.get_set_bits(i)

        print(f"Result: {math.floor(total_set_bits % (math.pow(10, 9) + 7))}")

    @classmethod
    def get_set_bits(cls, num):

        if num == 0:
            return 0
        return (1 if num & 1 == 1 else 0) + Solution.get_set_bits(num >> 1)


if __name__ == "__main__":
    Solution.solve(17)
    Solution.solve(4)
