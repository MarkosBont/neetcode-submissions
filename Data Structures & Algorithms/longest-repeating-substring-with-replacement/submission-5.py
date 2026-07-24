class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 0:
            return 0

        hmap = {}
        longest = 0

        left = 0

        for right in range(len(s)):
            hmap[s[right]] = hmap.get(s[right], 0) + 1

            if (right + 1 - left) - max(hmap.values()) > k:
                hmap[s[left]] -= 1
                left += 1
            
            longest = max(longest, right+1-left)
        
        return longest
        
        

        
        