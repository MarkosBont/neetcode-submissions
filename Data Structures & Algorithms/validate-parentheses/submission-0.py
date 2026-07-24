class Solution:
    def isValid(self, s: str) -> bool:
        l = []

        dictionary = {']':'[',
                      '}':'{',
                      ')':'('}

        for char in s:
            if char in dictionary:
                if not l or l.pop() != dictionary[char]:
                    return False
            
            else:
                l.append(char)

        return not l


        