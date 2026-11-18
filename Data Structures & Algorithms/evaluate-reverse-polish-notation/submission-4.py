class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        for val in tokens:
            if val == '+':
                result = int(stack.pop()) + int(stack.pop())
                stack.append(result)
            elif val == '-':
                right = int(stack.pop())
                left = int(stack.pop())
                result = left - right
                stack.append(result)
            elif val == '*':
                result = int(stack.pop()) * int(stack.pop())
                stack.append(result)
            elif val == '/':
                right = int(stack.pop())
                left = int(stack.pop())
                result = int(left / right)
                stack.append(result)
            else:
                stack.append(int(val))
    
        return stack.pop()