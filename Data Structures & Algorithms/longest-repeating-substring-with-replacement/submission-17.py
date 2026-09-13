class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        longest = 0
        hmap = {}

        for r in range(len(s)):
            hmap[s[r]] = hmap.get(s[r], 0) + 1

            curr_length = r - l + 1
            print(s[l], s[r], curr_length)
            if curr_length - max(hmap.values()) <= k:
                longest = max(longest, curr_length)
            
            else:
                hmap[s[l]] -= 1
                l += 1
        
        return longest
        