class Solution:
    def trap(self, height: List[int]) -> int:
        # can make an array same size of height, each index corresponds to the rain thatcan be trapped
        # water can be trapped in a position if neighbouring are bigger than itself
        # is this a sliding window problem?
        n = len(height)
        prefix = [0]*n
        suffix = [0]*n

        prefix[0] = height[0]
        suffix[n-1] = height[n-1]

        trappedRain = 0

        for i in range(1,n):
            prefix[i] = max(height[i], prefix[i-1])

        for i in range(n-2, -1, -1):
            suffix[i] = max(height[i], suffix[i+1])

        for i in range(n):
            trappedRain += min(suffix[i],prefix[i]) - height[i]
        
        return trappedRain

            
            

