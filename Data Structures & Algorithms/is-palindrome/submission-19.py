class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1
        s = s.lower()

        while left <= right:
            if s[left].isalnum() and s[right].isalnum() and s[left] == s[right]:
                left += 1
                right -= 1
            
            elif s[left].isalnum() and s[right].isalnum() and s[left] != s[right]:
                return False
            
            elif not s[left].isalnum():
                left += 1
            
            elif not s[right].isalnum():
                right -= 1
            
        return True
