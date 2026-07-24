class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 0:
            return 0

        left = 0
        longest = 1
        hmap = {}

        for right in range(len(s)):
            if s[right] not in hmap:
                hmap[s[right]] = 1

            else:
                while hmap[s[right]] > 0:
                    hmap[s[left]] -= 1
                    left += 1
                
                hmap[s[right]] = 1

            longest = max(longest, right + 1 - left)

                
        return longest



        