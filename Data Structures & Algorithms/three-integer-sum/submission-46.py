class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = set()
        nums.sort()
        
        for i in range(len(nums)):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            target = -nums[i]
            hmap = {}
            for j in range(i+1, len(nums)):

                num = nums[j]
                if target - num in hmap:
                    triplets.add((nums[i], nums[j], nums[hmap[target-num]]))
                else:
                    hmap[num] = j

        return [list(i) for i in triplets]


        