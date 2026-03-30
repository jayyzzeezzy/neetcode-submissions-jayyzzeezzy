class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        
        def dfs(i, comboArr, total):
            if total == target:
                res.append(comboArr.copy())
                return
            if total > target or i == len(candidates):
                return

            # decision 1: include candidates[i]
            comboArr.append(candidates[i])
            dfs(i + 1, comboArr, total + candidates[i])
            comboArr.pop()

            # decision 2: skip candidates[i]
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]: # make sure i is still in bound first
                i += 1
            dfs(i + 1, comboArr, total)

        dfs(0, [], 0)
        return res