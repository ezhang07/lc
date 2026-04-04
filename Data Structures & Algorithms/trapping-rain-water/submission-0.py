class Solution:
    def trap(self, height: List[int]) -> int:

        maxPre = [0]*len(height)
        maxPre[0] = height[0]
        maxSuf = [0]*len(height)
        maxSuf[len(height)-1] = height[len(height)-1]
        trapped = 0

        for i in range(1,len(height)):
            maxPre[i] = max(maxPre[i-1], height[i])
    #        prefix.append(maxPre)

        for i in range(len(height)-2, -1, -1):
            maxSuf[i] = max(maxSuf[i+1], height[i])
            

        for i in range(1, len(height)-1):
            trapped = trapped + min(maxPre[i],maxSuf[i]) - height[i]

        return trapped

        
