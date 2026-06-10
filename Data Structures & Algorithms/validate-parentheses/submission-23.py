class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {
            ")":"(",
            "]":"[",
            "}":"{"
        }

        stack = []
        for c in s:
            # close bracket
            if c in closeToOpen:
                # stack is not empty
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                # stack empty
                else:
                    return False

            # open bracket
            else:
                stack.append(c)

        return False if stack else True