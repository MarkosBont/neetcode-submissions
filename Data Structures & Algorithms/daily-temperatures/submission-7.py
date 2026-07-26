class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            if not stack or stack[-1][0] >= temp:
                stack.append([temp, i])
            
            while stack and stack[-1][0] < temp:
                result[stack[-1][1]] = i - stack[-1][1]
                stack.pop()
            
            stack.append([temp, i])

        return result


        