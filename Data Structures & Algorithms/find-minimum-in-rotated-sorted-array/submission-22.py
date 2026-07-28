class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        minimum = float('inf')

        while left <= right:
            if nums[left] < nums[right]:
                minimum = min(minimum, nums[left])
                break
                
            middle = (left + right) // 2
            minimum = min(minimum, nums[middle])

            if nums[middle] >= nums[left]:
                left = middle + 1
            
            else:
                right = middle - 1
        
        return minimum

        