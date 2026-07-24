class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = {}

        for s in strs:
            key = "".join(sorted(s))
            print(key)
            hmap[key] = hmap.get(key, [])
            hmap[key].append(s)
        
        return list(hmap.values())
        