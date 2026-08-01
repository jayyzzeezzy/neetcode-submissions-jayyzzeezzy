class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for idx, tmp in enumerate(temperatures):
            while stack and tmp > stack[-1][0]:
                stackTmp, stackIdx = stack.pop()
                res[stackIdx] = idx - stackIdx

            stack.append([tmp, idx])
        return res