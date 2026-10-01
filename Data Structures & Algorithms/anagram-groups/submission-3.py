class Solution: 
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)

        for s in strs:
            char_dist = [0] * 26
            for c in s:
                i = ord(c) - ord('a')
                char_dist[i] += 1
            
            anagram_map[tuple(char_dist)].append(s)
        
        return list(anagram_map.values())
        




