class Solution:

    def encode(self, strs: List[str]) -> str:
        res = "" 
        for s in strs:
            sLen = len(s)
            res = res + str(sLen) + '@' + s

        return res  

    def decode(self, s: str) -> List[str]:
        res = []
        val = ""
        i = 0
        length = ""


        while i < len(s):
            # get the length of the incoming string
            while ord(s[i]) - ord('0') <= 9:
                length += s[i]
                i += 1

            # skip over the '.'    
            i += 1

            # iterate over length of string, should give us the entire string
            j = 0 
            while j < int(length):
                val += s[i]
                j+=1
                i+=1
            
            res.append(val)
            length = ""
            val = ""

        return res