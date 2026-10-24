class Solution:
    def alnum_s(self, s):
            final = ""
            for char in s:
                if char.isalnum():
                    final += char
            
            return final

    def isPalindrome(self, s: str) -> bool:
        s = s.lower().strip()
        s = self.alnum_s(s)
        
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False
        return True
        



        