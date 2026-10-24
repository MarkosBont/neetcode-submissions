class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        openers = {')':'(',
                '}':'{',
                ']':'['}

        for char in s:
            if char not in openers:
                stack.append(char)
            
            else:
                if stack[-1] == openers[char]:
                    del stack[-1]

        return len(stack) == 0

        