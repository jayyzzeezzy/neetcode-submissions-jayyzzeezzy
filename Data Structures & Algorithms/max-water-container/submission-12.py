class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxA = 0
        l, r = 0, len(heights) - 1

        while l < r:
            curA = min(heights[l], heights[r]) * (r - l)
            maxA = max(maxA, curA)
            if heights[r] < heights[l]:
                r -= 1
            else:
                l += 1

        return maxA