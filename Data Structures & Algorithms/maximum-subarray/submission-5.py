class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curMax = 0
        globMax = nums[0] 

        for n in nums:
            curMax = max(curMax + n, n)
            globMax = max(globMax, curMax)
        return globMax