class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hmap = {}
        for char in s1:
            hmap[char] = hmap.get(char, 0) + 1
        
        left = 0
        for right in range(len(s2)):
            hmap[s2[right]] = hmap.get(s2[right], 0) - 1
            if hmap[s2[right]] == 0:
                del hmap[s2[right]]

            if right + 1 - left < len(s1):
                continue

            if not hmap:
                return True
            
            hmap[s2[left]] = hmap.get(s2[left], 0) + 1
            if hmap[s2[left]] == 0:
                del hmap[s2[left]]
            
            left += 1
        
        return False
            


        
