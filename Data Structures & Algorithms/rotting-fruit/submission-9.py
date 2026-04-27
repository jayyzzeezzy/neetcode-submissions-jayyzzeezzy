class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        fresh = 0
        q = collections.deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                if grid[r][c] == 1:
                    fresh += 1

        time = 0
        direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while fresh > 0 and q:
            for i in range(len(q)):
                row, col = q.popleft()
                for dr, dc in direction:
                    r, c = row + dr, col + dc
                    if (r in range(ROWS) and c in range(COLS) and grid[r][c] == 1):
                        grid[r][c] = 2
                        q.append((r, c))
                        fresh -= 1
            time += 1
        return time if fresh == 0 else -1