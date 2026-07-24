class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = defaultdict(int)

        for num in nums:
            hmap[num] += 1

        sorted_hmap = sorted(hmap.items(), key = lambda x: x[1], reverse = True)
        k_top = sorted_hmap[:k]

        final = []
        for i in k_top:
            final.append(i[0])
        
        return final
        