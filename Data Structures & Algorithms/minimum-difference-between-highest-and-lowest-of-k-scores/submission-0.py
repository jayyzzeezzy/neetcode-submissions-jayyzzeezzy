class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = float("inf")
        for l in range(len(nums) - k + 1):
            r = l + k
            diff = max(nums[l:r]) - min(nums[l:r])
            res = min(res, diff)

        return res
