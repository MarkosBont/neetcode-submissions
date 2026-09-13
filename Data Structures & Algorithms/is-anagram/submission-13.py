class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hmap_s = {}
        hmap_t = {}

        for char in s:
            hmap_s[char] = hmap_s.get(char, 0) + 1
        
        for char in t:
            hmap_t[char] = hmap_t.get(char, 0) + 1
        
        if len(hmap_s) != len(hmap_t):
            return False
        
        for key, value in hmap_s.items():
            if hmap_t.get(key, 0) != value:
                return False
        
        return True


        

        

        