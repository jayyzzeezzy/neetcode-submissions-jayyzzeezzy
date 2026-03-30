class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = { ")":"(", "]":"[", "}":"{" }
        stack = deque()

        for c in s:
            # close
            if c in closeToOpen:
                if stack:
                    if stack[-1] == closeToOpen[c]:
                        stack.pop()
                    else: return False
                else:
                    return False

            # open
            else: 
                stack.append(c)

        return False if stack else True