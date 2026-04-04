class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)

        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackTopPop = stack.pop()
                stackTemp = stackTopPop[0]
                stackInd = stackTopPop[1]
                res[stackInd] = i - stackInd
            
            stack.append((t,i))
        
        return res


