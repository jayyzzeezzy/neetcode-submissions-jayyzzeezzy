class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefixSum = []
        curSum = 0

        for n in nums:
            curSum += n
            prefixSum.append(curSum)

        total = prefixSum[-1]
        for i in range(len(prefixSum)):
            leftSum = prefixSum[i-1] if i > 0 else 0
            rightSum = total - prefixSum[i] if i < len(prefixSum) - 1 else 0
            if leftSum == rightSum:
                return i

        return -1