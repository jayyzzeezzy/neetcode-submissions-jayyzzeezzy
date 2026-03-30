class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {")":"(", "]":"[", "}":"{"}
        stack = []

        for c in s:
            # closing brackets
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            # opening brackets
            else:
                stack.append(c)

        return False if stack else True