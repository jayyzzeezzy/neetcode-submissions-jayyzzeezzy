class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        longest = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            longest = max(longest, len(charSet))
        return longest


        # seen = set()
        # longest = 0
        # l, r = 0, 0
        # while r < len(s):
        #     while s[r] in seen:
        #         seen.remove(s[l])
        #         l += 1
        #     seen.add(s[r])
        #     longest = max(longest, len(seen))
        #     r += 1
        # return longest