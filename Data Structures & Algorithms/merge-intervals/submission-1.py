class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        output = [intervals[0]]

        for start, end in intervals[1:]:
            recentEnd = output[-1][1]

            if start <= recentEnd:
                output[-1][1] = max(recentEnd, end)
            else:
                output.append([start, end])
        return output