class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        counter = {}
        for char in s:
            counter[char] = counter.get(char, 0) + 1
        
        for char in t:
            if char not in counter:
                return False
            else:
                counter[char] -= 1
                if counter[char] == 0:
                    del counter[char]
        
        return len(counter) == 0
                
        

            
        
        