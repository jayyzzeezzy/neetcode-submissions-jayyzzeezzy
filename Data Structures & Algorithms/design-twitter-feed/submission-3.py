class Twitter:

    def __init__(self):
        self.count = 0
        self.followMap = defaultdict(set)
        self.tweetMap = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # use Min Heap
        res = []
        minHeap = []
        self.followMap[userId].add(userId)

        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                lastIndex = len(self.tweetMap[followeeId]) - 1
                count, tweetId = self.tweetMap[followeeId][lastIndex]
                minHeap.append([count, tweetId, followeeId, lastIndex - 1])

        heapq.heapify(minHeap)
        while minHeap and len(res) < 10:
            count, tweetId, followeeId, lastIndex = heapq.heappop(minHeap)
            res.append(tweetId)
            if lastIndex >= 0:
                count, tweetId = self.tweetMap[followeeId][lastIndex]
                heapq.heappush(minHeap, [count, tweetId, followeeId, lastIndex - 1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
