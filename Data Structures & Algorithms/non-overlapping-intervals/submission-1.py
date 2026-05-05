class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        endpoint = intervals[0][1]

        res = 0
        for start, end in intervals[1:]:
            if start >= endpoint:
                endpoint = end
            else:
                res += 1
                endpoint = min(endpoint, end)

        return res