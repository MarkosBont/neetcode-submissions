class Solution:
    def makeUnique(self, s):
        final = [0] * 26
        for char in s:
            final[ord(char) - ord('a')] += 1
        
        return final

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = {}

        for s in strs:
            unique = tuple(self.makeUnique(s))
            hmap[unique] = hmap.get(unique, [])
            hmap[unique].append(s)


        return list(hmap.values())
        