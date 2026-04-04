class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        

        grouping = {}  # freqTable : anagrams


        
        for i, string in enumerate(strs):

            freqTable = [0]*26

            for j in range(len(string)):

                pos = ord(string[j]) - ord('a')

                freqTable[pos] = freqTable[pos]+1

            key = tuple(freqTable)

            if key in grouping:
                grouping[key].append(string)

            else:
                grouping[key] = [string]

        return list(grouping.values())


