class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output = [0 for _ in range(len(temperatures))]

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                index = stack[-1][0]
                output[index] = i - index
                stack.pop()
            
            stack.append((i, temp))
        
        return output

            
        