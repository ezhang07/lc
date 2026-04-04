class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        squares = defaultdict(set)

        for i in range(9):
            seen = set()
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in seen:
                    return False
                seen.add(board[i][j])

        for i in range(9):
            seen = set()
            for j in range(9):
                if board[j][i] == ".":
                    continue
                if board[j][i] in seen:
                    return False
                seen.add(board[j][i])

        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue
                if board[row][col] in squares[row//3,col//3]:
                    return False
                squares[row//3,col//3].add(board[row][col])
        
        return True
        

        