class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        no_duplicates = set(nums)
        sorted_list = sorted(list(no_duplicates))
        highest = 1
        for i in range(len(sorted_list)-1):
            if sorted_list[i] + 1 == sorted_list[i+1]:
                highest += 1

        return highest



        