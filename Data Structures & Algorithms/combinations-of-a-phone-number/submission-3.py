class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        numToChar = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }

        res = []
        def backtrack(i, curStr):
            if len(digits) == len(curStr):
                res.append(curStr)
                return

            for c in numToChar[digits[i]]:
                backtrack(i+1, curStr + c)

        if digits:
            backtrack(0, "")
            
        return res