class Solution:
    def isValid(self, s: str) -> bool:
        open_close = {'{':'}', '(':')', '[':']'}

        stack = []

        for char in s:
            if char in open_close:
                stack.append(char)
            
            else:
                if stack and open_close[stack[-1]] == char:
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0
        