class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hmap = {}
        for char in s1:
            hmap[char] = hmap.get(char, 0) + 1
        
        for right in range(len(s2)):
            hmap[s2[right]] = hmap.get(s2[right], 0) - 1

            if right >= len(s1):
                hmap[s2[right - len(s1)]] += 1
            
            if right >= len(s1) - 1:
                if all(v == 0 for v in hmap.values()):
                    return True
        
        return False








        