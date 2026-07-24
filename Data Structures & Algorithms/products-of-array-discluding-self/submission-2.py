class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        i=0

        while len(output) < len(nums):
            j=0
            product = 1

            while j < len(nums):
                if i != j:
                    product *= nums[j]

                j += 1
                     
            output.append(product)
            i += 1
        
        return output





        
        