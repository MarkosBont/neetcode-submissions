class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0 
        right = len(nums) - 1

        while left <= right:
            midpoint = (left + right) // 2
            element = nums[midpoint] 
            
            if target > element:
                left = midpoint + 1
            elif target < element:
                right = midpoint - 1
            
            else:
                return midpoint

        return -1

        