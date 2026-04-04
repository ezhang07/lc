class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for i in range(len(s)):
            if s[i] == '(':
                stack.append('(')
            if s[i] == '{':
                stack.append('{')
            if s[i] == '[':
                stack.append('[')
            if s[i] == ')':
                if len(stack) == 0:
                    return False
                if stack[-1] != '(':
                    return False
                else:
                    stack.pop()
            if s[i] == '}':
                if len(stack) == 0:
                    return False
                if stack[-1] != '{':
                    return False
                else:
                    stack.pop()
            if s[i] == ']':
                if len(stack) == 0:
                    return False
                if stack[-1] != '[':
                    return False
                else:
                    stack.pop()
        if len(stack) == 0:
            return True
        else:
            return False

        
        