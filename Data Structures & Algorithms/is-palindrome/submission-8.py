class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ""

        for char in s.lower():
            if char.isalnum(): 
                string += char

        pointer_a = 0
        pointer_b = len(string)-1

        while pointer_a < pointer_b:
            if string[pointer_a] == string[pointer_b]:
                pointer_a += 1
                pointer_b -= 1
            
            else:
                return False
        
        return True

        

        