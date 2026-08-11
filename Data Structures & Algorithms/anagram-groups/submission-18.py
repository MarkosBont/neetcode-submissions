class Solution:
    def make_tuple(self, s):
        counts = [0] * 26

        for char in s:
            counts[ord(char) - ord('a')] += 1

        return tuple(counts)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = {}

        for s in strs:
            tuple_s = self.make_tuple(s)
            hmap[tuple_s] = hmap.get(tuple_s, [])
            hmap[tuple_s].append(s)
        
        return list(hmap.values())
        