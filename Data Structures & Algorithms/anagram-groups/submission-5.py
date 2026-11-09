class Solution: 
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # use array of size 26 as signature
        # dict {signature : list of strings}

        anagram_map = defaultdict(list)

        for s in strs:
            signature = [0] * 26

            for c in s:
                signature[ord(c) - ord('a')] += 1
            
            anagram_map[tuple(signature)].append(s)
        
        return list(anagram_map.values())

        

        




