class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap = {}
        for n in nums:
            countMap[n] = 1 + countMap.get(n, 0)

        freq = [[] for i in range(len(nums) + 1)]
        for key, val in countMap.items():
            freq[val].append(key)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res