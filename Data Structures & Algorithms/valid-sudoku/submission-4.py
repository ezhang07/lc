class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        subBoxMap = defaultdict(set) # coordinates as tuples : seenSet

        for i in range(9):
            rowSet = set()
            for j in range(9):
                if board[i][j] == '.':
                    continue
                if board[i][j] in rowSet:
                    return False
                rowSet.add(board[i][j])

        for i in range(9):
            columnSet = set()
            for j in range(9):
                if board[j][i] == '.':
                    continue
                if board[j][i] in columnSet:
                    return False
                columnSet.add(board[j][i])

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                if board[i][j] in subBoxMap[(i // 3, j // 3)]:
                    return False
                subBoxMap[(i // 3, j // 3)].add(board[i][j])

        return True



            
                
