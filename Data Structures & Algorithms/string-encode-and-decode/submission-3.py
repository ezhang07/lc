class Solution:

    def encode(self, strs: List[str]) -> str:
        res = "" 
        for s in strs:
            res = res + str(len(s)) + '@' + s

        return res  

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            print("start", {i}, {j}) 

            while s[j] != '@':
                j+=1
            print(i,j)
            
            length = int(s[i:j])

            i = j + 1
            j = i + length
            val = s[i:j]
            print(i,j)

            res.append(val)
            
            i = j

        
        return res

            


