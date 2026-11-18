class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.min_stack:
            self.min_stack.append(val)
        
        elif self.min_stack:
            if self.min_stack[-1] >= val:
                self.min_stack.append(val)

    def pop(self) -> None:
        recent = self.stack[-1]
        recent_min = self.min_stack[-1]
        self.stack.pop()

        if self.min_stack:
            if recent_min == recent:
                self.min_stack.pop()  

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        
        return self.min_stack[-1]

        
