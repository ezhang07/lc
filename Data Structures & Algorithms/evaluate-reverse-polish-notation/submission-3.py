class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t == '+':
                firstOperand = stack[-1]
                stack.pop()
                secondOperand = stack[-1]
                stack.pop()
                result = secondOperand+firstOperand
                stack.append(result)
            elif t == '-':
                firstOperand = stack[-1]
                stack.pop()
                secondOperand = stack[-1]
                stack.pop()
                result = secondOperand-firstOperand
                stack.append(result)
            elif t == '*':
                firstOperand = stack[-1]
                stack.pop()
                secondOperand = stack[-1]
                stack.pop()
                result = secondOperand*firstOperand
                stack.append(result)
            elif t == '/':
                firstOperand = stack[-1]
                stack.pop()
                secondOperand = stack[-1]
                stack.pop()
                result = int(secondOperand/firstOperand)
                stack.append(result)
            else:
                stack.append(int(t))
        
        return stack[-1]
