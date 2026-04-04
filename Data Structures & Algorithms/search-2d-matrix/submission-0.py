class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        resList = []

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                resList.append(matrix[i][j])
                  
        
        
        l = 0
        r = len(resList)-1

        while l <= r:
            m = (l+r) // 2

            if resList[m] > target:
                r = m - 1
            elif resList[m] < target:
                l = m + 1
            else:
                return True
        
        return False
