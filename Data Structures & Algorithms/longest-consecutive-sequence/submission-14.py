class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        nums_set = set()
        for num in nums:
            nums_set.add(num)
        
        longest = 1

        for num in nums_set:
            if num-1 in nums_set:
                continue
            
            local_longest = 1
            for i in range(1, len(nums)):
                if num + i in nums_set:
                    local_longest += 1
                else:
                    break
            
            if local_longest > longest:
                longest = local_longest

            
        return longest


        




        