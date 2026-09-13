class Solution:
    def alNumVersion(self, s):
        final = ""
        for char in s:
            if char.isalnum():
                final += char

        return final

    def isPalindrome(self, s: str) -> bool:

        s = self.alNumVersion(s.lower().replace(' ', ''))
        left = 0
        right = len(s)-1

        while left <= right:
            if s[left] != s[right]:
                return False
            
            left += 1
            right -= 1
        
        return True



        