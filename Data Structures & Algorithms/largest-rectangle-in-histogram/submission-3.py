"""
if only 1 val in heights:
    return heights[0]

for loop heights from 2nd value:
    if the current height is >= last element in stack:
        append to stack the tuple (index, heights[i])
    else:
        pop from stack
        calculate area of popped bar, with its height * (i - popped index + 1) and compare to res
        append new height to stack, with popped index

return res

"""


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if len(heights) == 1:
            return heights[0]

        stack = [(0, heights[0])]
        res = 0
        
        for i in range(1,len(heights)):
            if heights[i] >= stack[-1][1]:
                stack.append((i, heights[i]))
            else:
                leftestPoppedIndex = 0
                while stack and heights[i] < stack[-1][1]:
                    poppedBar = stack.pop()
                    res = max(res, poppedBar[1] * (i - poppedBar[0]))
                    leftestPoppedIndex = poppedBar[0]
                
                stack.append((leftestPoppedIndex, heights[i]))
        
        while stack:
            poppedBar = stack.pop()
            res = max(res, poppedBar[1] * (len(heights) - poppedBar[0]))
        
        return res


"""
- initial approach: use two pointers, beside the current height, and stop when either heights on pointers
are smaller/reach the end of list

for loop checking bar's height, range from 2nd element to 2nd last element:
    while loop for left pointer in bounds (>0) and greater than curheight:
        move to left, update width, update res

    while loop for right pointer in bounds (<len(heights)-1) and greater than curHeight:
        move to right, update width, update res

return res

new approach: using monotonic stack. 
- record the height and corresponding index for each bar, res/maxArea
- for loop, if current height < next height to right, then the rectangle is still valid,
if not then get area, compare to res and pop.
    - if there is a pop, the next height on the right is added to stack, with the popped value's index,
    because it has a smaller height to begin with, so the bar on the left would be part of its rectangle
- 
edge case: only 1 val in heights


"""