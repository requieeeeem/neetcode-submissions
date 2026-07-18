class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set) #normal dict would give keyerror without valid key
        cols = collections.defaultdict(set)
        square = collections.defaultdict(set)

        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue
                if (board[row][col] in rows[row] or #check with row hash set to see if it's already in that row
                    board[row][col] in cols[col] or #check with col hash set to see if it's already in that col
                    board[row][col] in square[(row//3): (col//3)]): 
                    #check with square dict to see if it's already in the square (pair of row // 3: col //3)
                    return False
                else:
                    #add num to that row hash set in rows
                    rows[row].add(board[row][col])
                    #add num to that col hash set in cols
                    cols[col].add(board[row][col])
                    #add num to that square hash set in square
                    square[(row // 3): (col // 3)].add(board[row][col])

        return True

                