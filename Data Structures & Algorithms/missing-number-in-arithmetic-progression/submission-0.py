class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        n = len(arr)
        difference = (arr[n-1] - arr[0]) // n

        lo = 0
        hi = n - 1
        while lo < hi:
            m = (lo + hi) // 2
            if arr[m] == arr[0] + difference * m:
                lo = m + 1
            else:
                hi = m

        return arr[0] + difference * lo