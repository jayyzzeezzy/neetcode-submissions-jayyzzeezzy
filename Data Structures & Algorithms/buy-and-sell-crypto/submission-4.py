class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        l, r = 0, 1
        while r < len(prices):
            profit = prices[r] - prices[l]
            maxP = max(maxP, profit)
            if prices[l] > prices[r]:
                l = r
            r += 1

        return maxP