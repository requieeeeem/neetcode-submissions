class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        top, bot = 0, rows - 1

        while top <= bot:
            row = (top + bot) // 2 #to find correct row
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break

        low, high = 0, cols - 1

        while low <= high:
            col = (low + high) // 2
            if target > matrix[row][col]:
                low = col + 1
            elif target < matrix[row][col]:
                high = col - 1
            else:
                return True
        
        return False