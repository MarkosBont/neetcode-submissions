class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = {}

        for s in strs:
            sort_s = "".join(sorted(s))
            hmap[sort_s] = hmap.get(sort_s, [])
            hmap[sort_s].append(s)
        
        return list(hmap.values())
        