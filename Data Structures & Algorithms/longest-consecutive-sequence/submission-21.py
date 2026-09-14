class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        all_nums = set()

        for num in nums:
            all_nums.add(num)
        
        for num in nums:
            if num-1 in all_nums:
                continue
            
            else:
                length = 1
                while num+1 in all_nums:
                    length += 1
                    num = num+1
                
                longest = max(longest, length)
        
        return longest


        