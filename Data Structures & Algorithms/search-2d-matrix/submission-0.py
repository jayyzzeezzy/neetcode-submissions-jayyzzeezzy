class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        
        top, bot = 0, ROWS - 1
        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break

        if not (top <= bot): # target is not found in all rows
            return False

        # find the row that contains target
        row = (top + bot) // 2

        l, r = 0, COLS - 1
        while l <= r:
            m = l + ((r - l) // 2)
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else: 
                return True

        return False # target is not in the current row