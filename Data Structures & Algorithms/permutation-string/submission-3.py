class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        countS1 = self.getAscii(s1)
        l, r = 0, len(s1)

        while r < len(s2)+1:
            subString = self.getAscii(s2[l:r])

            if countS1 == subString:
                return True

            l+=1
            r+=1
        return False
        
    def getAscii(self, s):
        count = [0] * 26
        for c in s:
            count[ord(c) - ord("a")] += 1
        return count