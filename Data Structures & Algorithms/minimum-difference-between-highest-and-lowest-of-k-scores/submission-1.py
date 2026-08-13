class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = float("inf")
        for l in range(len(nums) - k + 1):
            r = l + k - 1
            diff = nums[r] - nums[l]
            res = min(res, diff)

        return res
