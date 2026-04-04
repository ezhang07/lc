class Solution:
    def trap(self, height: List[int]) -> int:
        # can make an array same size of height, each index corresponds to the rain thatcan be trapped
        # water can be trapped in a position if neighbouring are bigger than itself
        # is this a sliding window problem?

        trapped = [0]*len(height)

        for i in range(1,len(height)-1):
            l = i
            r = i
            greatestL = 0
            greatestR = 0

            while l >= 0:
                greatestL = max(greatestL, height[l])
                l-=1

            while r <= len(height)-1:
                greatestR = max(greatestR, height[r])
                r+=1

            trapped[i] = min(greatestL,greatestR) - height[i]
        
        maxRain = 0

        for n in trapped:
            maxRain+=n
        
        return maxRain
            
            

