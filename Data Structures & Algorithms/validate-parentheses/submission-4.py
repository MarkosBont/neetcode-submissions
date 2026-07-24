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
                if stack and stack[-1] == openers[char]:
                    del stack[-1]
                else:
                    return False

        return len(stack) == 0

        