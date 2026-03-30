class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        visit = set()

        def safe(r, c):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or
                board[r][c] == "X" or
                board[r][c] == "T"
            ):
                return

            board[r][c] = "T"
            safe(r-1, c)
            safe(r+1, c)
            safe(r, c-1)
            safe(r, c+1)

        def dfs(r, c):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or
                (r, c) in visit or
                board[r][c] == "X"
            ):
                return

            visit.add((r, c))
            board[r][c] = "X"
            dfs(r-1, c)
            dfs(r+1, c)
            dfs(r, c-1)
            dfs(r, c+1)

        for c in range(COLS):
            safe(0, c)
            safe(ROWS-1, c)
        
        for r in range(ROWS):
            safe(r, 0)
            safe(r, COLS-1)
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    dfs(r, c)

                if board[r][c] == "T":
                    board[r][c] = "O"