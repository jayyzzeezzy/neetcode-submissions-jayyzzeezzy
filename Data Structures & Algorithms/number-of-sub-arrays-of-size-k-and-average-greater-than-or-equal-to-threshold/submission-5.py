class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        curSum = 0
        res = 0
        l = 0

        for r in range(len(arr)):
            if (r - l + 1) > k:
                curSum -= arr[l]
                l += 1

            if (r - l + 1) < k:
                curSum += arr[r]
                continue
                
            curSum += arr[r]
            average = curSum / k
            if average >= threshold:
                res += 1

        return res