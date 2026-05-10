class Solution:
    def isValid(self, s: str) -> bool:
        brackMap = {
            ")":"(",
            "]":"[",
            "}":"{"
        }
        stack = []
        for char in s:
            # close bracket
            if char in brackMap:
                # 2 outcomes
                if stack and stack[-1] == brackMap[char]:
                    stack.pop()
                else:
                    return False

            # open bracket
            else:
                stack.append(char)
        return False if stack else True