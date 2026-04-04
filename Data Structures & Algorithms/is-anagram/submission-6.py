class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        freqTable1 = {}
        freqTable2 = {}

        for i in range(len(s)):
            freqTable1[s[i]] = freqTable1.get(s[i],0) + 1
            freqTable2[t[i]] = freqTable2.get(t[i],0) + 1
        
        return freqTable1 == freqTable2
            
        