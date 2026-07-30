class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        l = 0

        hashmap = {}

        for r in range(len(s)):
            hashmap[s[r]] = hashmap.get(s[r], 0) + 1
            if (r - l + 1) - max(hashmap.values()) > k:
                hashmap[s[l]] -= 1
                l += 1
            
            longest = max(longest, r - l + 1)
        
        return longest