class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        maxC = 0
        l = 0
        r = 0
        
        while r < len(s):
            count[s[r]] = count.get(s[r],0)+1
            maxC = max(maxC, count[s[r]])

            while r-l+1 - maxC > k:
                count[s[l]] = count[s[l]] - 1
                l+=1
            
            res = max(res, r-l+1)
            r+=1
        
        return res