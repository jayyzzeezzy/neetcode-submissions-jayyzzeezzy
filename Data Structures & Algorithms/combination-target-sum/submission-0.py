class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        # array = []
        def dfs(i, array, total):
            if total == target:
                res.append(array.copy())
                return
            if i >= len(nums) or total > target:
                return

            # decision 1: add new number
            array.append(nums[i])
            dfs(i, array, total + nums[i])
            # decision 2: do not add said number
            array.pop()
            dfs(i + 1, array, total)

        dfs(0, [], 0)
        return res