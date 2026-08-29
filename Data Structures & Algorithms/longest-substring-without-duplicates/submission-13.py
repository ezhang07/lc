class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        :type s: str
        :rtype: int

        sliding window,
        increment right pointer if no repeat chars
        sets for repeats lookup
        increment left pointer if repeat, until no more repeat.
        res will always be like -1, when returning, add 1 to res !!! 
        """

        res = 1
        l = 0
        r = 1

        if len(s) == 0:
            return len(s)
        
        seen = set(s[0])

        while r < len(s):
            if s[r] not in seen:
                seen.add(s[r])
                res = max(res, r - l + 1)
                r += 1
            else:
                while s[l] != s[r]:
                    seen.remove(s[l])
                    l += 1
                # once the same value, just inc left pointer and also right pointer
                l += 1
                r += 1
            
        return res