class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        rowZero = False

        # mark the work
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    # set 1st row to 0
                    matrix[0][c] = 0

                    # set 1st col to 0 but skip rowZero
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        rowZero = True

        # do the work starting at index 1
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        # finish the work at index 0
        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0

        if rowZero:
            for c in range(COLS):
                matrix[0][c] = 0