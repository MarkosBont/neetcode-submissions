class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 1

        set_of_nums = set(nums)

        for num in set_of_nums:
            if num-1 in set_of_nums:
                continue
            else:
                start = num
                for i in range(1, len(nums)):
                    if num+i in set_of_nums:
                        longest += 1
        

        return longest


        