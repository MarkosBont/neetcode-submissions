class Solution:
    def isValid(self, s):
        openers = {'(': ')', '[': ']', '{': '}'}

        stack = []

        for char in s:
            if char in openers:
                stack.append(char)
            else:
                if not stack or openers[stack[-1]] != char:
                    return False
                stack.pop()

        return len(stack) == 0

        