class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hmap  = {}
        for c in s1:
            hmap[c] = hmap.get(c,0) + 1

        l = 0
        for r in range(len(s2)):
            hmap[s2[r]] = hmap.get(s2[r], 0) - 1
            if hmap[s2[r]] == 0:
                del hmap[s2[r]]

            if r + 1 < len(s1):
                continue
            
            if len(hmap) == 0:
                return True
            
            hmap[s2[l]] = hmap.get(s2[l], 0)+ 1
            if hmap[s2[l]] == 0:
                del hmap[s2[l]]
            
            l += 1
        
        return False
            

            
        