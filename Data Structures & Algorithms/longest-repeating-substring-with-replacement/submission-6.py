class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap = {}
        longest = 0

        l = 0

        for r in range(len(s)):
            hashmap[s[r]] = hashmap.get(s[r], 0) + 1
            length = r - l + 1

            if length - max(hashmap.values()) > k:
                l += 1
            
            else:
                longest = max(longest, length)
        
        return longest
