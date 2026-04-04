class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        anagramMap1 = {}
        anagramMap2 = {}
        for i in range(len(s)):
           # if s[i] not in anagramMap1:
            anagramMap1[s[i]]= anagramMap1.get(s[i],0)+1
            anagramMap2[t[i]]= anagramMap2.get(t[i],0)+1
        return anagramMap1 == anagramMap2
        