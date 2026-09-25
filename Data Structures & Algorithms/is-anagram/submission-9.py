class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        dictionary, char : frequency
        edge case: s and t not same length -> return false

        approach:
        make dictionaries for s and t

        iterate over s and t, at each index, we want to add to the dictionary, to specific char's frequency

        after iterating over, we can check equality on dictionaries
        """

        freq_map_s = {}
        freq_map_t = {}

        for c in s: # adding to the char's frequency in string s
            freq_map_s[c] = freq_map_s.get(c, 0) + 1
        
        for c in t: # doing same thign for string t
            freq_map_t[c] = freq_map_t.get(c, 0) + 1
        
        return freq_map_s == freq_map_t
        