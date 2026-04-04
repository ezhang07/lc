class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(len(board)):
            dupe = set()

            for j in range(len(board)):
                

                if board[i][j] == ".":
                    continue
                if board[i][j] in dupe:
                    return False

                dupe.add(board[i][j])

        for i in range(len(board)):
            dupe = set()
            for j in range(len(board)):
                

                if board[j][i] == ".":
                    continue
                if board[j][i] in dupe:
                    return False

                dupe.add(board[j][i])
        
        squares = defaultdict(list)

        for i in range(len(board)):

            for j in range(len(board)):

                if board[i][j] == ".":
                    continue

                if board[i][j] in squares[(i//3,j//3)]:
                    return False

                squares[(i//3,j//3)].append(board[i][j])
        
        return True
                
        
            