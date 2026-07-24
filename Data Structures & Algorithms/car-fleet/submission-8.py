class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        joined = [(position[i], speed[i]) for i in range(len(speed))]
        joined = sorted(joined, key = lambda x:x[0], reverse=True)

        stack = []
        for pair in joined:
            time = (target-pair[0])/pair[1]
            if not stack or time > stack[-1]:
                stack.append(time)

        return len(stack) 

                
