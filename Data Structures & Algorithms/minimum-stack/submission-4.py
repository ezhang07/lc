class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if self.minStack: # if minStack has stuff in it, then just check for new min val
            val = min(val, self.minStack[-1]) 
        self.minStack.append(val) # always append val. so stack and minStack are same len
        # first append for minStack defaults to the initial value

        
    
    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]
        
