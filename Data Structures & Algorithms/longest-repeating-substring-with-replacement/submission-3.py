class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        longest = 0

        hmap = {}

        for right in range(len(s)):
            hmap[s[right]] = hmap.get(s[right], 0) + 1

            while len(s[left:right]) + 1 - max(hmap.values()) > k:
                hmap[s[left]] -= 1
                left += 1
            
            longest = max(longest, len(s[left:right])+1)

        return longest





            
            
        