class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxRain = 0

        for i in range(len(heights)):
            for j in range(len(heights)):
                minHeight = min(heights[i],heights[j])
                width = j-i
                maxRain = max(maxRain, width*minHeight)
        
        return maxRain
        