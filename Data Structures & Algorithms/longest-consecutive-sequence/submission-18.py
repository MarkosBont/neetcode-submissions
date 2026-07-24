class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        longest = 1

        for num in nums:
            local_longest = 1
            if num-1 in nums:
                continue
            
            counter = 1
            while num + counter in nums:
                local_longest += 1
                longest = max(longest, local_longest)
                counter += 1

        return longest
                
            


        