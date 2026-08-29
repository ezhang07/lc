class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        bracketMap = {'}' : '{', ']': '[', ')' : '('} # hash table correspods closing bracket to opening bracket

        for i, b in enumerate(s): 
            if b in bracketMap: # if closing bracket, means we pop to see top of stack, see if that's the corresponding bracket
                if stack:
                    opening = stack.pop()
                else:
                    return False
                if opening != bracketMap[b]:
                    return False
            else:
                stack.append(b)

        if stack:
            return False
        
        return True
                
