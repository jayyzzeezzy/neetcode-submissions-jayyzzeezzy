class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): 
            return False

        oneMap = {}
        for s in s1:
            oneMap[s] = 1 + oneMap.get(s, 0)

        twoMap = {}
        l, r = 0, 0
        while r < len(s2):
            # Maintain a window of size len(s1)
            twoMap[s2[r]] = 1 + twoMap.get(s2[r], 0)

            if (r - l + 1) == len(s1):
                if twoMap == oneMap:
                    return True
                
                # Shrink window from left
                twoMap[s2[l]] -= 1
                if twoMap[s2[l]] == 0:
                    del twoMap[s2[l]]
                l += 1
            
            r += 1

        return False