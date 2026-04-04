class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        minLen = float('inf')
        minLP = 0

        freqMap = {}

        for c in t:
            freqMap[c] = freqMap.get(c, 0) + 1
        
        for r in range(len(s)):

            if s[r] in freqMap:
                l = r
                rp = r
                copyMap = {}

                while rp < len(s) and copyMap != freqMap:

                    if s[rp] in freqMap:
                        if freqMap[s[rp]] > copyMap.get(s[rp],0):
                            copyMap[s[rp]] = copyMap.get(s[rp],0) + 1
                    
                    rp+=1

                if copyMap == freqMap:
                    if rp-l+1 < minLen:
                        minLen = rp-l+1
                        minLP = l

        
        return s[minLP: minLP+minLen-1] if minLen != float('inf') else ""