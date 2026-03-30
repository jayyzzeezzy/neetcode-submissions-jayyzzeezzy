class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        count = {}
        requirement = len(nums) / 2

        for n in nums:
            count[n] = 1 + count.get(n, 0)

        for val in count.values():
            if count.get(target, 0) > requirement:
                return True
        
        return False