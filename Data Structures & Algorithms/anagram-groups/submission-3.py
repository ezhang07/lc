class Solution(object):
    def groupAnagrams(self, strs):
        freqTable = defaultdict(list) # freq array: list of anagrams

        for i in range(len(strs)):
            freqArray = [0]*26
            for c in strs[i]:
                freqArray[ord(c) - ord('a')] += 1
            
            freqTable[tuple(freqArray)].append(strs[i])
            
        return list(freqTable.values())
            

        