class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closers = {'}':'{',
                  ']': '[',
                  ')': '('}

        for char in s:
            if char not in closers:
                stack.append(char)
            else:
                if stack and stack[-1] == closers[char]:
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0



        