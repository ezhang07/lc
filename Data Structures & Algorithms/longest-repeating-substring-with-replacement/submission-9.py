class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l = 0

        charMap = {}
        res = 0
        maxCharFreq = 0
        for r in range(len(s)):
            charMap[s[r]] = charMap.get(s[r], 0) + 1
            maxCharFreq = max(maxCharFreq, max(charMap.values()))
            curLen = 0



            while (r-l+1)-maxCharFreq > k:
                charMap[s[l]] = charMap.get(s[l],0)-1
                l+=1
                curLen-=1
            
            res = max(res, (r-l+1))
        
        return res



            # checking for key with max occurences,
            # if everything - key with max is <= k, then it's considered valid
            # if not valid, l+=1, remove one from the value at that key


        