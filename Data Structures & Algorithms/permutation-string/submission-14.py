class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hmap = {}
        for char in s1:
            hmap[char] = hmap.get(char, 0) + 1
        
        if len(s1) > len(s2):
            return False
        
        l = 0

        for r in range(len(s2)):
            hmap[s2[r]] = hmap.get(s2[r], 0) - 1
            if hmap[s2[r]] == 0:
                del hmap[s2[r]]
            
            if r < len(s1)-1:
                continue
            
            if not hmap:
                return True
            
            hmap[s2[l]] = hmap.get(s2[l], 0) + 1
            if hmap[s2[l]] == 0:
                del hmap[s2[l]]
            
            l += 1
        
        return False
        