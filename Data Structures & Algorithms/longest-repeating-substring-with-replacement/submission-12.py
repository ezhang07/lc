class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        :type s: str
        :type k: int
        :rtype: int

        sliding window approach
        hash table as char freq map
        keep on inc right ptr as long as k replacements can be made within hashmap, and most freq char is the baseline
        substringLen - mostFreqChar < k, keep inc right ptr
        > k, need to change sliding window size, inc left ptr, until k replacements can be made again
        """

        res = 0
        mostFreqChar = 0
        charMap = {}
        l = 0

        for r in range(len(s)):
            charMap[s[r]] = charMap.get(s[r], 0) + 1
            mostFreqChar = max(mostFreqChar, charMap[s[r]])

            while (r - l + 1) - mostFreqChar > k:
                charMap[s[l]] -= 1
                l += 1
            
            res = max(res, (r - l + 1))
        
        return res

    


        