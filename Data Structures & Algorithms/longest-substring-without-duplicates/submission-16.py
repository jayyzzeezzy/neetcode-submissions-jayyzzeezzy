class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        string = set()
        l, r = 0, 0
        longest = 0

        while r < len(s):
            while s[r] in string:
                string.remove(s[l])
                l += 1
            string.add(s[r])
            longest = max(longest, len(string))
            r += 1

        return longest