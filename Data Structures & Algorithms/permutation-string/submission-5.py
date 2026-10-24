class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hmap = {}
        for char in s1:
            hmap[char] = hmap.get(char, 0) + 1
        
        l = 0
        
        for r in range(len(s2)):
            if s2[r] in hmap:
                hmap[s2[r]] -= 1
                if all(v == 0 for v in hmap.values()):
                    return True
            
            if r >= len(s1):
                l += 1
        
        return False
            
            


        