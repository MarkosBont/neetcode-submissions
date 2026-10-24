class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []

        for i in range(len(nums)):
            target = -nums[i]
            if i > 1 and nums[i] == nums[i-1]:
                continue
            
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if nums[left] + nums[right] < target:
                    left += 1
                    while nums[left-1] == nums[left]:
                        left += 1
                
                elif nums[left] + nums[right] > target:
                    right -= 1
                    while nums[right] == nums[right+1]:
                        right -= 1
                
                else:
                    triplets.append([-target, nums[left], nums[right]])
                    right -= 1
                    left += 1

                    while nums[right] == nums[right+1]:
                        right -= 1

                    while nums[left-1] == nums[left]:
                        left += 1
        
        return triplets

        