class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr = [[p, s] for p, s in zip(position, speed)]
        arr.sort(reverse=True)
        stack = []

        for p, s in arr:
            time = (target - p) / s
            if not stack or time > stack[-1]:
                stack.append(time)

        return len(stack)