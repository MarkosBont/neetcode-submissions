class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = {}
        longest = 0
        left = 0

        for right in range(len(s)):
            hashmap[s[right]] = hashmap.get(s[right], 0) + 1
            while hashmap[s[right]] == 2:
                hashmap[s[left]] -= 1
                left += 1
            
            longest = max(longest, right + 1 - left)
        
        return longest

        