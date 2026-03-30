class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        count = 0
        for n in nums:
            count = count + 1 if n == target else count
        return count > len(nums) // 2