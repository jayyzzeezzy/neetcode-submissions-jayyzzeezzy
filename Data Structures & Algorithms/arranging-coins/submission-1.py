class Solution:
    def arrangeCoins(self, n: int) -> int:
        remainingCoins = n
        rows = 0
        for i in range(1, n):
            remainingCoins -= i

            if remainingCoins < 0:
                return rows
                
            rows += 1

        return 1 if n == 1 else rows