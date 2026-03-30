class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums) # final value in nums

        for i in range(len(nums)):
            res += (i - nums[i])
        return res