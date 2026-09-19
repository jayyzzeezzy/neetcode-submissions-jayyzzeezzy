class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        counts = defaultdict(int)
        l, total, res = 0, 0, 0

        for r in range(len(fruits)):
            counts[fruits[r]] += 1
            total += 1

            while len(counts) > 2:
                f = fruits[l]
                counts[f] -= 1
                total -= 1
                l += 1
                if not counts[f]:
                    counts.pop(f)

            res = max(res, total)

        return res