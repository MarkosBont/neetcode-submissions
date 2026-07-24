class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}

        for num in nums:
            hmap[num] = hmap.get(num, 0) + 1
        
        sorted_hmap = sorted(hmap.items(), key = lambda x: x[1], reverse = True)

        k_sorted_hmap = sorted_hmap[:k]

        final_array = []
        for x in k_sorted_hmap:
            final_array.append(x[0])

        return final_array
        