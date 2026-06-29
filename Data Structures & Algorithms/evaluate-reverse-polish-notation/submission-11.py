class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            if c == "+":
                firstN, secondN = stack.pop(), stack.pop()
                stack.append(firstN + secondN)
            elif c == "*":
                firstN, secondN = stack.pop(), stack.pop()
                stack.append(firstN * secondN)
            elif c == "-":
                firstN, secondN = stack.pop(), stack.pop()
                stack.append(secondN - firstN)
            elif c == "/":
                firstN, secondN = stack.pop(), stack.pop()
                stack.append(int(secondN / firstN))
            else:
                stack.append(int(c))
        return stack[0]