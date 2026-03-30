class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles) # binary search k from the smallest to the biggest pile value
        res = r # make the answer (k) equal to the biggest pile as worst case scenario

        while l <= r:
            k = (l + r) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / k) 

            if hours <= h: # valid answer but can we go smaller k
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1

        return res