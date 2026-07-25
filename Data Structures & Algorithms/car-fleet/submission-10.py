class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []

        cars = [(position[i], speed[i]) for i in range(len(position))]
        cars.sort(key = lambda x:x[0])
        
        for i in range(len(cars)-1, -1, -1):
            if not stack:
                stack.append(cars[i])
                continue
            
            in_stack = stack[-1]
            in_stack_time = (target- in_stack[0]) / in_stack[1]

            this_car = cars[i]
            this_car_time = (target- this_car[0]) / this_car[1]

            if this_car_time > in_stack_time:
                stack.append(this_car)

        return len(stack)
            

        