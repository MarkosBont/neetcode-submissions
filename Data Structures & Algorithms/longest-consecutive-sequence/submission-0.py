class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        no_duplicates = set(nums)
        sorted_list = sorted(list(no_duplicates))
        print(sorted_list)
        highest = 1
        for i in range(len(sorted_list)-1):
            if sorted_list[i] + 1 == sorted_list[i+1]:
                highest += 1

        return highest



        