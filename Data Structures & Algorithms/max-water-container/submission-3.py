class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        :type height: List[int]
        :rtype: int

        left pointer approach, move pointer depending on which one is shorter maybe? 
        each iteration, record:
        width (r - l)
        which is bigger between l and r, 
        what happens if l and r are equal? 
        max Area (always check this)
        """

        maxArea = 0

        l = 0
        r = len(heights) - 1

        while l < r:
            width = r - l
            maxArea = max(maxArea, width * min(heights[l], heights[r]))

            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
            
        return maxArea


        