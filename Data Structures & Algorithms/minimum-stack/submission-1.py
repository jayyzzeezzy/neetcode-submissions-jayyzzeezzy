class MinStack:

    def __init__(self):
        self.array = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.array.append(val)
        if self.minStack:
            val = min(val, self.minStack[-1])
        self.minStack.append(val)

    def pop(self) -> None:
        self.array.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.array[-1]

    def getMin(self) -> int:
        return self.minStack[-1]