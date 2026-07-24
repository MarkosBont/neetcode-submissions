class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        longest = 1

        set_of_nums = set(nums)

        for num in set_of_nums:
            local_longest = 1
            if num-1 in set_of_nums:
                continue
            else:
                while num + local_longest in set_of_nums:
                    local_longest += 1
                
                if local_longest > longest:
                    longest = local_longest
        
        return longest


        