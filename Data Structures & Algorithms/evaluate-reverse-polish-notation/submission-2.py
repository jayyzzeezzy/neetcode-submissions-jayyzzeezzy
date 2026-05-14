import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == "+":
                first, second = stack.pop(), stack.pop()
                stack.append(first + second)
            elif c == "*":
                first, second = stack.pop(), stack.pop()
                stack.append(first * second)
            elif c == "-":
                first, second = stack.pop(), stack.pop()
                stack.append(second - first)                
            elif c == "/":
                first, second = stack.pop(), stack.pop()
                stack.append(int(second / first))
            else:
                stack.append(int(c))

        return stack[0]