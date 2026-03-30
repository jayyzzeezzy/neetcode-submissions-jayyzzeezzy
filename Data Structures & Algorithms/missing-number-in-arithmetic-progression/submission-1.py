class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        n = len(arr)
        difference = (arr[n-1] - arr[0]) // n

        start = 0
        end = n - 1
        while start < end:
            m = (start + end) // 2
            # go right, move start
            if arr[m] == arr[0] + m * difference:
                start = m + 1
            else:
                # go left, move end
                end = m
        return arr[0] + start * difference