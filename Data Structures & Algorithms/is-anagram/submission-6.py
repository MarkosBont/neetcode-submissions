class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hmap = {}

        for char in s:
            hmap[char] = hmap.get(char, 0) + 1
        
        for char in t:
            if char in hmap:
                hmap[char] -= 1
                if hmap[char] == 0:
                    del hmap[char]
            else:
                return False
        
        return len(hmap) == 0
        