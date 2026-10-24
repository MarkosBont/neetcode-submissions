def contains_duplicate(s):
    seen = set()
    for char in s:
        if char in seen:
            return True
        seen.add(char)
    
    return False

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 1
        MaxCounter = 0
        local_count = 0

        while right < len(s):
            if contains_duplicate(s[left:right]):
                local_count = 0
                left += 1
            else:
                local_count += 1
                MaxCounter = max(MaxCounter, local_count)
                right += 1
        
        return MaxCounter
                
        


            
        