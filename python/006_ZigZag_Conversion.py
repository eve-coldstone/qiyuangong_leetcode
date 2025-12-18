class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s
        # char array
        rows = [''] * numRows
        curRow = 0
        goingDown = False

        for c in s:
            rows[curRow] += c
            if curRow == 0 or curRow == numRows - 1:
                goingDown = not goingDown
            curRow += 1 if goingDown else -1

        return ''.join(rows)
        
if __name__ == '__main__':
    obj = Solution()
    s = "PAYPALISHIRING"
    print(f"Result is : ", obj.convert(s,3))