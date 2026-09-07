class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        target = k * threshold
        curSum = sum(arr[:k-1])
        res = 0

        for i in range(len(arr) - k + 1):
            curSum += arr[i + k - 1]
            if curSum >= target:
                res += 1

            curSum -= arr[i]

        return res