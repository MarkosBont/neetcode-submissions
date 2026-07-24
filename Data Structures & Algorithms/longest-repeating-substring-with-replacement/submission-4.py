class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        hmap = {}

        l = 0

        for r in range(len(s)):
            hmap[s[r]] = hmap.get(s[r], 0) + 1

            while (r - l + 1) - max(hmap.values()) > k:
                hmap[s[l]] -= 1
                l += 1
            
            longest = max(longest, r-l+1)
        
        return longest

        
        
        