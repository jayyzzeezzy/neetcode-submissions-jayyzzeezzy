class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        L, R = 0, 0
        total, res = 0, 0

        while R < len(nums):
            total += nums[R]

            while nums[R] * (R - L + 1) > total + k:
                total -= nums[L]
                L += 1
            
            res = max(res, R - L + 1)
            R += 1

        return res