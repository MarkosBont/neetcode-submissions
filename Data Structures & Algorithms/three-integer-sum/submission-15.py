class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = set()

        for i in range(len(nums)):
            target = -nums[i]

            left = i + 1
            right = len(nums) - 1

            while left < right:
                if nums[left] + nums[right] == target:
                    output.add(tuple(sorted([nums[left], nums[right], nums[i]])))
                    left += 1
                    right -= 1

                elif nums[left] + nums[right] < target:
                    left += 1
                
                else:
                    right -= 1

        return list(list(l) for l in output)
                    


            
        