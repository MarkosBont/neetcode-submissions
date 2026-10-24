class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        minimum = float('inf')

        while l <= r:
            middle =(l+r) // 2
            minimum = min(minimum, nums[middle])

            if nums[middle] < nums[r]:
                r = middle
            
            elif nums[middle] > nums[r]:
                l = middle + 1
            
            if middle == r:
                break
        
        return minimum
        


        