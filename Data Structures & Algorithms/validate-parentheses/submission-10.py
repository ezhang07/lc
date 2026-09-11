class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parenthesesMap = {')' : '(', ']' : '[', '}' : '{'}

        for p in s:
            if p in parenthesesMap:
                if stack and stack[-1] == parenthesesMap[p]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(p)
        
        if not stack:
            return True
        return False


                
