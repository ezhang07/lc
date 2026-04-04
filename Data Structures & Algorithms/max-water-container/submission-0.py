class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxWater = 0
        l = 0
        r = len(heights)-1

        while l < r:
            width = r - l
            height = min(heights[l], heights[r])

            if (width*height) < maxWater:
                if height == heights[l]:
                    l+=1
                else:
                    r-=1
            else:
                maxWater = width*height
                if height == heights[l]:
                    l+=1
                else:
                    r-=1
        
        return maxWater