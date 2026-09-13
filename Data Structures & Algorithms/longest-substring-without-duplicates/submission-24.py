class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hmap = {}
        maxLength = 0
        left = 0

        for right in range(len(s)):
            hmap[s[right]] = hmap.get(s[right], 0) + 1

            while hmap[s[right]] == 2:
                hmap[s[left]] -= 1
                left += 1
            
            maxLength = max(maxLength, right - left + 1)
            
        return maxLength
                

            


