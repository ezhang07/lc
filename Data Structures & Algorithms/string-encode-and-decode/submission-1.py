class Solution:

    def encode(self, strs: List[str]) -> str:
        res = "" 
        for s in strs:
            res+=s
            res = res + "."

        return res  
            
    def decode(self, s: str) -> List[str]:
        res = []
        val = ""
        for c in s:
            if c == ".":
                res.append(val)
                val = ""
                continue
            val+=c
        return res