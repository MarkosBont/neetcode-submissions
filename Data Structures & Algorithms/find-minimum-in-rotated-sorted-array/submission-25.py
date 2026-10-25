class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            midpoint = (left + right) // 2
            if nums[midpoint] > nums[right]:
                left = midpoint + 1
            elif nums[midpoint] < nums[right]:
                right = midpoint 

        if left == right:
            return nums[left]

        