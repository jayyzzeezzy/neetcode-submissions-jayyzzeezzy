class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevPos = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevPos:
                return [prevPos[diff], i]

            prevPos[n] = i