class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()

        def modCell(r, c):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or
                grid[r][c] == "0"
            ):
                return 
            grid[r][c] = "0"
            q.append((r, c))

        islands = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    grid[r][c] = "0"
                    q.append((r, c))
                    islands += 1

                    while q:
                        r, c = q.popleft()
                        modCell(r-1, c)
                        modCell(r+1, c)
                        modCell(r, c-1)
                        modCell(r, c+1)
                        
        return islands