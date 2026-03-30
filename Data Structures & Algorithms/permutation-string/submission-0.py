class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)

        if len(s1) > len(s2): return False

        s1Counts = [0] * 26
        s2Counts = [0] * 26

        for i in range(n1):
            s1Counts[ord(s1[i]) - ord('a')] += 1
            s2Counts[ord(s2[i]) - ord('a')] += 1

        if s1Counts == s2Counts: 
            return True

        for i in range(n1, n2):
            s2Counts[ord(s2[i]) - ord('a')] += 1
            s2Counts[ord(s2[i - n1]) - ord('a')] -= 1
            if s1Counts == s2Counts: 
                return True

        return False