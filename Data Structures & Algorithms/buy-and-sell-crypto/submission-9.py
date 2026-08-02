class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        l = 0
        for r in range(len(prices)):
            profit = prices[r] - prices[l]
            maxP = max(maxP, profit)
            if prices[r] < prices[l]:
                l = r
                
        return maxP