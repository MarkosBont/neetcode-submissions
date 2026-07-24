def is_num(token):
    try:
        int(token)
        return True

    except ValueError:
        return False

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if is_num(token):
                stack.append(int(token))
            
            else:
                if token == "+":
                    result = stack.pop() + stack.pop()
                    stack.append(result)
                elif token == "-":
                    first_pop = stack.pop()
                    second_pop = stack.pop()
                    result = second_pop - first_pop
                    stack.append(result)
                
                elif token == "*":
                    
                    result = stack.pop() * stack.pop()
                    stack.append(result)
                
                elif token == "/":
                    first_pop = stack.pop()
                    second_pop = stack.pop()
                    result = int(second_pop / first_pop)
                    stack.append(result)
                
                print(stack)
                
        return stack[-1]


        