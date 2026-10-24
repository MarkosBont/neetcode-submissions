class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(nums) - 1

        while l < r:
            while not s[l].isalnum() and l < r:
                l += 1
            
            while not s[r].isalnum() and l < r:
                r -= 1
            
            if s.lower()[l] != s.lower([r]):
                return False
        
        return True

        

        