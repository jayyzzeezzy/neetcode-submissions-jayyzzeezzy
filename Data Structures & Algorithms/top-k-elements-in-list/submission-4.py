class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = defaultdict(list)
        freq = [ [] for i in range(len(nums) + 1)]

        for i, n in enumerate(nums):
            res[n] = 1 + res.get(n, 0)
        for key, val in res.items():
            freq[val].append(key)

        output = []
        for i in range(len(freq) -1, 0, -1):
            for j in freq[i]:
                output.append(j)
                if len(output) == k:
                    return output