class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0


        set_of_nums = set(nums)

        for num in set_of_nums:
            longest = 1
            if num-1 in set_of_nums:
                continue
            else:
                start = num
                print(start)
                while num + longest in set_of_nums:
                    longest += 1
        
        return longest


        