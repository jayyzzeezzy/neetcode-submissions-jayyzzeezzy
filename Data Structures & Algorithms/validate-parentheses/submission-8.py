class Solution:
    def isValid(self, s: str) -> bool:
        hashMap = {"(":")", "[":"]", "{":"}"}
        stack = []

        if len(s) % 2: return False

        for c in s:
            if c in hashMap:
                stack.append(c)
            else:
                if stack:
                    bracket = stack.pop()
                    if c != hashMap[bracket]:
                        return False
                else:
                    return False

        return False if stack else True