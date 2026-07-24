class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()

        for i in range(len(nums)-1):
            left = i+1
            right = len(nums) - 1
            target = -nums[i]

            while left < right:
                if nums[left] + nums[right] == target:
                    output.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                elif nums[left] + nums[right] < target:
                    left += 1

                elif nums[left] + nums[right] > target:
                    right -= 1


        sorted_output = []
        for l in output:
            sorted_l = sorted(l)
            sorted_output.append(sorted_l)

        output_set = set([tuple(l) for l in sorted_output])

        return list([list(l) for l in output_set])


            




            


        


        