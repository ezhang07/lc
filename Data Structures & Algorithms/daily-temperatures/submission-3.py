class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        initial thoughts:
        monotonic decreasing stack
        in stack, record index and temperature pair

        in for loop, wanna check whether temperature at index i is larger than top of stack
        if this is the case, then we have found the warmer temperature
        we pop it and put the result into the res array, only possible with the index-temp pair
        after we've gone through the while loop, means either no more vals in stack or all remaining temps  are >=, so append to stack
        """

        res = [0] * len(temperatures)
        stack = [] # [index: temperature]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                stackIndex, stackTemp = stack.pop()
                res[stackIndex] = i - stackIndex
            stack.append([i, t])
        
        return res


