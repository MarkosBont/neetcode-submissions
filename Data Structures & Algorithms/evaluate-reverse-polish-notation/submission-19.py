class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token.strip('-').isalnum():
                stack.append(int(token))
            
            else:
                if token == "+":
                    result = stack.pop() + stack.pop()
                    stack.append(result)
                
                elif token == "-":
                    first = stack.pop()
                    second = stack.pop()
                    result = second - first
                    stack.append(result)
                
                elif token == "*":
                    result = stack.pop() * stack.pop()
                    stack.append(result)
                
                else:
                    first = stack.pop()
                    second = stack.pop()
                    result = int(second / first)
                    stack.append(result)
        
            
        return stack[-1]
        