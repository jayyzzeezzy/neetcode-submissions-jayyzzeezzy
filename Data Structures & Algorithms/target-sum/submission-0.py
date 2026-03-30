class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)
        dp[0] = 1

        for i in range(len(nums)):
            newDP = defaultdict(int)
            for cur_sum, count in dp.items():
                newDP[cur_sum + nums[i]] += count
                newDP[cur_sum - nums[i]] += count
            dp = newDP
        return dp[target]