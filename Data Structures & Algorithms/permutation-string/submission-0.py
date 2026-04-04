class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        permutationMap = {}

        for c in s1:
            permutationMap[c] = 1 + permutationMap.get(c, 0)
        
        l = 0

        for r in range(len(s1)-1, len(s2)):
            windowMap = {}

            for i in range(l, r+1):
                windowMap[s2[i]] = 1 + windowMap.get(s2[i],0)
            
            if windowMap == permutationMap:
                return True
            
            l+=1
        
        return False
            



        
