class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        left = 0	
        hmap = {}
        
        for char in s1:
            hmap[char] = hmap.get(char, 0) + 1

        for i, char in enumerate(s2):
            hmap[char] = hmap.get(char, 0) - 1

            if hmap[char] == 0:
                del hmap[char]	

            if i >= len(s1):
                hmap[s2[left]] = hmap.get(s2[left], 0) + 1
                
                if hmap[s2[left]] == 0:
                    del hmap[s2[left]]
                
                left += 1
            
            if len(hmap) == 0:
                return True
                    
        return False
		


        