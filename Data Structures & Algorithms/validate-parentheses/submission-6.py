class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        bracketMap = {']':'[', ')':'(','}':'{'}

        for c in s:
            if c not in bracketMap:
                stack.append(c)
            else:
                if stack and stack[-1] == bracketMap[c]:
                    stack.pop()
                    continue
                else:
                    return False
            
        if not stack:
            return True
        else:
            return False
                
