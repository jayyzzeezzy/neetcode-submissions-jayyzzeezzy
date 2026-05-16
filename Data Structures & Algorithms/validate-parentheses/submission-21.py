class Solution:
    def isValid(self, s: str) -> bool:
        bracketMap = {
            ")":"(",
            "]":"[",
            "}":"{"
        }
        stack = []

        for c in s:
            # close bracket
            if c in bracketMap:
                # stack is not empty
                if stack and stack[-1] == bracketMap[c]:
                    stack.pop()
                # stack is empty
                else:
                    return False

            # open bracket
            else:
                stack.append(c)

        return False if stack else True