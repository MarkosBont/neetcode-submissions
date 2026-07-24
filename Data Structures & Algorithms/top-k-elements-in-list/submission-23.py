class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = [[] for i in range(len(nums)+1)]
        used = 0
        output = []
        
        hmap = {}
        for num in nums:
            hmap[num] = hmap.get(num, 0) + 1
        
        print(hmap)
        
        for key, value in hmap.items():
            counts[value].append(key)
        
        for i in range(len(counts)-1, -1, -1):
            if counts[i]:
                for num in counts[i]:
                    output.append(num)
                    used += 1
                    if used == k:
                        return output