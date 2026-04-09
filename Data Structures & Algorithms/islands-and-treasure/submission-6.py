class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        q = collections.deque()
        visit = set()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))

        direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        step = 0
        while q:
            for i in range(len(q)):
                row, col = q.popleft()
                grid[row][col] = step
                for dr, dc in direction:
                    r, c = row + dr, col + dc
                    if (r in range(ROWS) and
                        c in range(COLS) and
                        (r, c) not in visit and
                        grid[r][c] != -1 and
                        grid[r][c] != 0
                    ):
                        visit.add((r, c))
                        q.append((r, c))
            step += 1