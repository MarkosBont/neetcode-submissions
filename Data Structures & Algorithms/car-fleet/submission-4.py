class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []

        for i in range(len(position)):
            cars.append((position[i], speed[i]))
        
        cars.sort(key=lambda x:x[0])

        stack = []

        for i in range(len(cars)-1, -1, -1):
            stack.append((cars[i]))

            if len(stack) > 1:
                top = stack[-1]
                second = stack[-2]

                top_time = (target-top[0])/top[1]
                second_time = (target-second[0])/second[1]

                if top_time <= second_time:
                    stack.pop()
                
        
        return len(stack)


            
            





        