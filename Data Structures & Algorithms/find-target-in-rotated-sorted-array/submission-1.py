class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            middle = (l+r) // 2
            if nums[middle] == target:
                return middle
            
            if nums[middle] >= nums[l]:
                if target > nums[middle] or target < nums[l]:
                    l = middle + 1
                else:
                    r = middle - 1

            else:
                if target < nums[middle] or target > nums[r]:
                    r = middle - 1
                else:
                    l = middle + 1
        
        return -1 



        