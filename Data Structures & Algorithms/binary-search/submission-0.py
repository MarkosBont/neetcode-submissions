class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        middle = r+l//2

        while l <= r:
            middle = (r + l) //2
            if target == nums[middle]:
                return middle
            
            elif target < nums[middle]:
                r = middle - 1
            
            else:
                l = middle + 1
        
        return -1
            


        