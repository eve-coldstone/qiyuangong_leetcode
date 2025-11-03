import math

class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s
        rows = [''] * numRows
        curRow = 0
        goingDown = False

        for c in s:
            rows[curRow] += c
            if curRow == 0 or curRow == numRows - 1:
                goingDown = not goingDown
            curRow += 1 if goingDown else -1

        return ''.join(rows)
    
    def convert_visual(self, s, numRows):
        if numRows == 1:
            return [s]

        cycleLen = 2*numRows - 2
        n = len(s)
        numCycles = math.ceil(n / cycleLen)
        # Estimate max columns
        colsPerCycle = numRows - 1
        numCols = numCycles * colsPerCycle

        # Initialize grid
        grid = [[' ' for _ in range(numCols)] for _ in range(numRows)]

        row, col = 0, 0
        i = 0
        while i < n:
            # Down
            while row < numRows and i < n:
                grid[row][col] = s[i]
                row += 1
                i += 1
            row -= 2
            col += 1
            # Up
            while row > 0 and i < n:
                grid[row][col] = s[i]
                row -= 1
                col += 1
                i += 1

        # Convert rows to strings
        result = [''.join(r).rstrip() for r in grid]
        return result

if __name__ == '__main__':
    s = Solution()
    print (s.convert("PAYPALISHIRING", 4))
    for r in s.convert_visual("PAYPALISHIRING", 4):
        print (r)


