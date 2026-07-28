class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [0 for _ in range(len(nums))]

        left = 1
        for i in range(len(nums)):
            result[i] = left
            left = left*nums[i]
        
        right = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] *= right
            right = right*nums[i]
        
        return result


        