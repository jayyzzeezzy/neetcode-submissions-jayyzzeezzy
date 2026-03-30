class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-n for n in stones]
        heapq.heapify(maxHeap)
        
        while len(maxHeap) > 1:
            x = heapq.heappop(maxHeap)
            y = heapq.heappop(maxHeap)
            
            if x < y: # compare negative values
                diff = x - y
                heapq.heappush(maxHeap, diff)

        maxHeap.append(0) # if list becomes empty
        return abs(maxHeap[0])