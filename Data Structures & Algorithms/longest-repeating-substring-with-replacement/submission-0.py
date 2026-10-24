class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        left = 0
        right = 1
        maxLength = 0

        local_length = 0

        while right < len(s):
            hmap = {}
            string = s[left:right]

            for char in string:
                hmap[char] = hmap.get(char, 0) + 1

            if len(string) - max(hmap.values()) < k:
                local_length += 1
                maxLength = max(maxLength, local_length)
                right += 1
            
            else:
                left += 1
        
        return maxLength




            
            
        