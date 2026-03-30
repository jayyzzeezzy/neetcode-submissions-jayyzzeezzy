class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
            
        dp = set()
        dp.add(0)
        target = sum(nums) // 2

        for i in range(len(nums) - 1, -1, -1):
            tempDP = set()
            for t in dp:
                # optional optimization
                if (t + nums[i] == target):
                    return True
                tempDP.add(t)
                tempDP.add(t + nums[i])

            dp = tempDP
            
        return True if target in dp else False