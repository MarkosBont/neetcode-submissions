class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 0:
            return 0

        left = 0
        longest = 1
        seen = set()

        for right in range(len(s)):
            if s[right] not in seen:
                seen.add(s[right])
                longest = max(longest, right + 1 - left)

            else:
                seen.remove(s[left])
                left += 1
        
        return longest



        