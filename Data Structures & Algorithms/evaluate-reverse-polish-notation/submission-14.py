class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token.isalnum():
                stack.append(int(token))
            
            else:
                if token == "+":
                    result = stack.pop() + stack.pop()
                    stack.append(result)
                
                elif token == "-":
                    result = stack.pop() - stack.pop()
                    stack.append(result)
                
                elif token == "*":
                    result = stack.pop() * stack.pop()
                    stack.append(result)
                
                else:
                    result = int(stack.pop() / stack.pop())
                    stack.append(result)
            
        return stack[-1]
        