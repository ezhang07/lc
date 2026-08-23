class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freqMapS = {}
        freqMapT = {}

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            freqMapS[s[i]] = freqMapS.get(s[i], 0) + 1
            freqMapT[t[i]] = freqMapT.get(t[i], 0) + 1
        
        return freqMapS == freqMapT