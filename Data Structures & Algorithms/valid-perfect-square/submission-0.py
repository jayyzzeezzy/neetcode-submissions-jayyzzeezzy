class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l, r = 0, num
        while l <= r:
            m = (l + r) // 2
            if m**2 > num:
                r = m - 1
            elif m**2 < num:
                l = m + 1
            else:
                return True
        return False