import math

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        carPosSpeed = []
        stack = []
        for i in range(len(position)):
            carPosSpeed.append((position[i],speed[i]))
        
        carPosSpeed.sort()

        for i in range(len(position)):
            stack.append((math.ceil(target-carPosSpeed[i][0])/carPosSpeed[i][1]))

        res = 0

        while stack:
            timeTilDest = stack.pop()
            while stack and stack[-1] <= timeTilDest:
                stack.pop()
            res+=1
        
        return res









        """
        - Stack that holds positions of cars, top -> highest starting pos
        - Stack should hold tuple? pos and corresponding speed
        - Condition to check whether top position is > target, then we pop, and check whether next 
        is going to be part of fleet

        """