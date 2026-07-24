class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}

        for num in nums:
            hmap[num] = hmap.get(num, 0) + 1
        
        sorted_map = sorted(hmap.items(), key=lambda x:x[1], reverse = True)

        k_sorted_map = sorted_map[:k]

        final_list = []
        for i in k_sorted_map:
            final_list.append(i[0])
        
        return final_list

        
        

        