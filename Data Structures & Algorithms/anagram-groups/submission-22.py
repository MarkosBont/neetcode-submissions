class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = {}
        for s in strs:
            sorted_s = sorted(s)
            sorted_s = "".join(sorted_s)
            if sorted_s in hmap:
                hmap[sorted_s].append(s)
            
            else:
                hmap[sorted_s] = [s]
        
        final_ans = []
        for key, val in hmap.items():
            final_ans.append(val)
        
        return final_ans

        