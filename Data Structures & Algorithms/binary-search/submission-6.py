class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l+r) // 2
            result = nums[mid]
            if result == target:
                return mid
            
            elif result > target:
                r = mid - 1
            
            else:
                l = mid + 1
        
        return - 1


        