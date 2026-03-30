class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-n for n in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)

            if x < y:
                diff = x - y
                heapq.heappush(stones, diff)

        stones.append(0)
        return abs(stones[0])