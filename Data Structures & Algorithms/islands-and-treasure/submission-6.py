class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        q = collections.deque()

        def modCell(r, c):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or
                (r, c) in visit or
                grid[r][c] == -1
            ):
                return
            visit.add((r, c))
            q.append((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visit.add((r, c))

        step = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = step
                modCell(r-1, c)
                modCell(r+1, c)
                modCell(r, c-1)
                modCell(r, c+1)
            step += 1