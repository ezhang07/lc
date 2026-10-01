class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        sliding window approach
        l = 0, r 
        hashset: keep track of values we've seen
        longestLength var

        if not char we've seen before, move right ptr
        add char to hashset, and update longestLength

        if we have, 
        move left ptr until repeat is no longer there
        remove curr value at left ptr from hashset 
        until value on right ptr is not in the hashset
        """

        if len(s) == 0:
            return 0
        
        seen = set()
        longest_len = 0
        l = 0

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            longest_len = max(longest_len, r - l + 1)
        
        return longest_len

