class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        wordMap = {}
        freq = [[] for n in range(len(nums) + 1)]

        for n in nums:
            wordMap[n] = 1 + wordMap.get(n, 0)

        for key, val in wordMap.items():
            freq[val].append(key)

        res = []
        for i in range(len(freq) -1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res