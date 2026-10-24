class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        for i, num in enumerate(nums):
            other_num = target  - num 

            if other_num in hmap:
                return [hmap[other_num], i]
            
            hmap[num] = i

        