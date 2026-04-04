class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l = 0
        r = 1
        maxLen = 0

        if len(s) >= 1:
            seen.add(s[0])
            maxLen = 1
        else:
            return 0

        while r < len(s):
            if s[r] in seen:

                while s[r] in seen:
                    seen.remove(s[l])
                    l+=1
                
            else:
                seen.add(s[r])
                r+=1
                if len(seen) > maxLen:
                    maxLen = len(seen)
        
        return maxLen