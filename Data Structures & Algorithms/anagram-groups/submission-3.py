def sort_s(s):
    return "".join(sorted(s))

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = {}

        for s in strs:
            key = sort_s(s)
            hmap[key] = hmap.get(key, [])
            hmap[key].append(s)
        
        return list(hmap.values())



            
        