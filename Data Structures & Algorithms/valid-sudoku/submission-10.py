class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSets = defaultdict(set)
        colSets = defaultdict(set)
        squareSets = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue

                if (board[r][c] in rowSets[r] or
                    board[r][c] in colSets[c] or
                    board[r][c] in squareSets[(r//3, c//3)]
                ):
                    return False

                rowSets[r].add(board[r][c])
                colSets[c].add(board[r][c])
                squareSets[(r//3, c//3)].add(board[r][c])

        return True