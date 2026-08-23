class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        globMax, globMin = nums[0], nums[0]
        curMax, curMin = 0, 0
        total = 0

        for n in nums:
            total += n

            curMax = max(curMax + n, n)
            globMax = max(globMax, curMax)

            curMin = min(curMin + n, n)
            globMin = min(globMin, curMin)
        
        return max(globMax, total - globMin) if globMax > 0 else globMax