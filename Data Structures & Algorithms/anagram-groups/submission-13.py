class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = {}

        for string in strs:
            sorted_string = "".join(sorted(string))
            hmap[sorted_string] = hmap.get(sorted_string, [])
            hmap[sorted_string].append(string)

        
        return list(hmap.values())

        