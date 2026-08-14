class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket = defaultdict(int)
        curSum, res = 0, 0
        
        l, r = 0, 0
        while r < len(fruits):
            basket[fruits[r]] += 1
            curSum += 1

            while len(basket) > 2:
                f = fruits[l]
                basket[f] -= 1
                curSum -= 1
                l += 1

                if not basket[f]:
                    basket.pop(f)

            res = max(res, curSum)

            r += 1

        return res