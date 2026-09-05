class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        curSum = 0
        res = 0
        l = 0

        for i in range(k-1):
            curSum += arr[i]

        for i in range(len(arr) - k + 1):
            curSum += arr[i + k - 1]
            average = curSum / k

            if average >= threshold:
                res += 1

            curSum -= arr[i]
        return res