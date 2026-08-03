class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower().replace(' ', '')
        final = ""

        for char in s:
            if char.isalnum():
                final += char
        
        return final == final[::-1]
