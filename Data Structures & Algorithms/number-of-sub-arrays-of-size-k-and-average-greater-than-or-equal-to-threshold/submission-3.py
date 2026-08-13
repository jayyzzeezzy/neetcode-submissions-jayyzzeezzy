class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0

        for l in range(len(arr) - k + 1):
            r = l + k
            subset = arr[l:r]

            if sum(subset) / k >= threshold:
                res += 1

        return res