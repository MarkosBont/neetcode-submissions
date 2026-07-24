class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}

        for i, num in enumerate(nums):
            wanted = target - num
            if wanted in hmap:
                return [hmap[wanted], i]
            
            hmap[num] = i


        