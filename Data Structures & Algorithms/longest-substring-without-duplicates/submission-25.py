class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0

        left = 0
        hmap = {}

        for right in range(len(s)):
            hmap[s[right]] = hmap.get(s[right], 0) + 1

            while hmap[s[right]] > 1:
                hmap[s[left]] -= 1
                left += 1
            longest = max(longest, right + 1 - left)
        
        return longest
                

        