class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hmap = {}
        for char in s1:
            hmap[char] = hmap.get(char, 0) + 1

        l = 0

        for r in range(len(s2)):
            hmap[s2[r]] = hmap.get(s2[r], 0) - 1

            if r - l >= len(s1):
                hmap[s2[l]] += 1
                l += 1
            
            if all(v == 0 for v in hmap.values()):
                return True
        
        return False
            


            
        