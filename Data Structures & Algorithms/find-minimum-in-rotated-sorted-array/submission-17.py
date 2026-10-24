class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        minimum = float('inf')

        while left <= right:
            middle = (left + right) // 2

            if nums[right] < nums[middle]:
                left = middle + 1
            
            elif nums[right] >= nums[middle] and nums[left] >= nums[middle]:
                minimum = nums[middle]
                break
            
            else:
                right = middle - 1
        
        return minimum

        