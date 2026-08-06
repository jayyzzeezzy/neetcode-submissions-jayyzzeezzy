class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l <= r:
            m = (r+l) // 2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                # go left
                r = m - 1
            else:
                # go right
                l = m + 1

        return -1