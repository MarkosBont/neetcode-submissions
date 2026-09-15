class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            if not stack or stack[-1][0] > temp:
                stack.append((temp, i))
            
            else:
                while stack and stack[-1][0] < temp:
                    t, index = stack.pop()
                    output[index] = i - index
                
                stack.append((temp, i))
        
        return output


            

        