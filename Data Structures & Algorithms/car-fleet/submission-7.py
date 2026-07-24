class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        joined = [(position[i], speed[i]) for i in range(len(speed))]
        joined = sorted(joined, key = lambda x:x[0])

        stack = []
        for i in range(len(joined)-1, -1, -1):
            stack.append(joined[i])
            while len(stack) > 1:
                first = stack[-1]
                first_time = (target - first[0])/first[1]  

                second = stack[-2]
                second_time = (target - second[0])/second[1] 

                if first_time <= second_time:
                    stack.pop()
                else:
                    break

        return len(stack) 

                
