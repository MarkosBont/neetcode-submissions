def is_num(num):
    try:
        int(num)
        return True
    except ValueError:
        return False

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for char in tokens:
            if is_num(char):
                stack.append(int(char))

            elif char == '+':
                addition = stack.pop() + stack.pop()
                stack.append(addition)

            elif char == '-':
                first = stack.pop()
                second = stack.pop()
                stack.append(second - first)
            
            elif char == '*':
                first = stack.pop()
                second = stack.pop()
                stack.append(second * first)

            elif char == '/':
                first = stack.pop()
                second = stack.pop()
                stack.append(int(second / first))
            
            print(stack)
            
        return stack[-1]

