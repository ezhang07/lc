class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t == '+':
                operand = stack[-1]
                stack.pop()
                stack[-1] = stack[-1]+ operand
            elif t == '-':
                operand = stack[-1]
                stack.pop()
                stack[-1] = stack[-1] - operand
            elif t == '*':
                operand = stack[-1]
                stack.pop()
                stack[-1] = stack[-1] * operand
            elif t == '/':
                operand = stack[-1]
                stack.pop()
                stack[-1] = int(stack[-1] / operand)
            else:
                stack.append(int(t))
        
        return stack[-1]
