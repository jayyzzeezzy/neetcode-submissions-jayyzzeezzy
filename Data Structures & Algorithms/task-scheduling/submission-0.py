class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
        q = collections.deque()
        time = 0

        while maxHeap or q:
            time += 1
            if maxHeap:
                cnt = heapq.heappop(maxHeap) + 1
                if cnt:
                    # q stores [count, idleTime]
                    q.append([cnt, n + time])

            if q and q[0][1] == time:
                # get the count
                addBack = q.popleft()[0]
                heapq.heappush(maxHeap, addBack)

        return time