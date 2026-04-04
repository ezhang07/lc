class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l = 0

        charMap = {}
        res = 0
        for r in range(len(s)):
            charMap[s[r]] = charMap.get(s[r], 0) + 1
            maxCharFreq = 0
            curLen = 0

            for key, v in charMap.items():
                maxCharFreq = max(maxCharFreq, v) 
                curLen+=v

            while curLen-maxCharFreq > k:
                charMap[s[l]] = charMap.get(s[l],0)-1
                l+=1
                curLen-=1
            
            res = max(res, curLen)
        
        return res



            # checking for key with max occurences,
            # if everything - key with max is <= k, then it's considered valid
            # if not valid, l+=1, remove one from the value at that key



            # can be optimized. curLen is just window size, which can be found with r - l + 1. 
            # instead of for loop at line 13 to find max value in hashmap values, can just do max(hashmap.values())
    


        