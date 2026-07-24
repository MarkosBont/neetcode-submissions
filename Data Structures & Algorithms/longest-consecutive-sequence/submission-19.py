class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        maximum = 0

        for num in nums:
            seen.add(num)

        for num in seen:
            if num - 1 in seen:
                continue
            
            length = 1
            i = 1
            while num + i in seen:
                length += 1
                i += 1
            
            maximum = max(maximum, length)

        return maximum
            
        