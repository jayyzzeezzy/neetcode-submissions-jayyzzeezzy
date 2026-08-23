class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = 0
        globMax = nums[0]

        for n in nums:
            curSum = max(curSum + n, n)
            # curSum += n
            globMax = max(globMax, curSum)
        return globMax