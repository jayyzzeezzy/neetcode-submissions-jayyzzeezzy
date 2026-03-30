class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        self.fresh, self.time = 0, 0
        q = deque()

        def rot(r, c):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or
                grid[r][c] != 1
            ):
                return
            grid[r][c] = 2
            q.append((r, c))
            self.fresh -= 1
            

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    self.fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))

        while q and self.fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                rot(r-1, c)
                rot(r+1, c)
                rot(r, c-1)
                rot(r, c+1)
            self.time += 1
        return self.time if self.fresh == 0 else -1