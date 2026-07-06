class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [[p, s] for p, s in zip(position, speed)]
        pairs.sort(reverse=True)

        stack = []
        stack.append((target - pairs[0][0]) / pairs[0][1])
        for p, s in pairs[1:]:
            arriveTime = (target - p) / s
            
            if stack and stack[-1] < arriveTime:
                stack.append(arriveTime)

        return len(stack)