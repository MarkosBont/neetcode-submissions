class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1

        seen = set()

        left = 0
        maxCounter = 0
        local_count = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
                local_count = local_count - 1

            seen.add(s[right])
            local_count += 1
            maxCounter = max(maxCounter, local_count)
        
        return maxCounter


                
        


            
        