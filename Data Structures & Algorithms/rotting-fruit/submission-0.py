class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = collections.deque()
        time, self.fresh = 0, 0

        def markRotten(r, c):
            if (r < 0 or c < 0 or r == ROWS or c == COLS or grid[r][c] != 1):
                return
            grid[r][c] = 2
            q.append([r,c])
            self.fresh -= 1

        for r in range(ROWS):
            for c in range(COLS):
                if (grid[r][c] == 2):
                    q.append([r, c])
                if (grid[r][c] == 1):
                    self.fresh += 1

        while q and self.fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                # go to each index and mark rotten
                markRotten(r - 1,c)
                markRotten(r + 1,c)
                markRotten(r,c - 1)
                markRotten(r,c + 1)
            time += 1

        return time if self.fresh == 0 else -1