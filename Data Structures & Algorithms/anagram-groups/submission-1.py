class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        freqTable = defaultdict(list)

        for i in range(len(strs)):
            freqList = [0]*26

            for c in strs[i]:
                freqList[ord(c)-97]+=1
            
            freqTable[tuple(freqList)].append(strs[i])
            
        

        
        return list(freqTable.values())
                
