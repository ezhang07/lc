class Solution:
    def isPalindrome(self, s: str) -> bool:
        # remove cpaitals .lower() .replace('x','o') ascii, 97-122
        s = s.lower().replace(" ","")
        newS = ""
        for c in s:
            if ord('a') <= ord(c) <= ord('z') or ord('0') <= ord(c) <= ord('9'):
                newS+=c
        
        l=0
        r=len(newS)-1

        while l<r:
            if newS[l] == newS[r]:
                l+=1
                r-=1
                continue
            return False
        
        return True


        