class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()

        for i in range(len(nums) -1):
            target = -nums[i]
            left = i+1
            right = len(nums) - 1

            while left < right:
                total = nums[left] + nums[right]
                if total == target:
                    output.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                
                elif total < target:
                    left += 1
                
                elif total > target:
                    right -= 1


        for s in output:
            s.sort()

        removed_duplicates = set(tuple(triple) for triple in output)

        return list(removed_duplicates)
            


        


        