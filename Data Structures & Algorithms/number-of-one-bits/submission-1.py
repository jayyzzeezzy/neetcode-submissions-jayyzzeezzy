class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n: # n != 0
            n = n & (n - 1)
            res += 1
        return res

        # res = 0
        # while n:
        #     res += n % 2 # return either 1 or 0
        #     n = n >> 1
        # return res 