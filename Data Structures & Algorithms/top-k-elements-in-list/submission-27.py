class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums)+1)]
        output = []

        hmap = {}
        for num in nums:
            hmap[num] = hmap.get(num, 0) + 1
        
        for num, freq in hmap.items():
            buckets[freq].append(num)
        
        for i in range(len(buckets)-1, -1, -1):
            for j in range(len(buckets[i])-1, -1, -1):
                if not k:
                    return output
                output.append(buckets[i][j])
                k -= 1
        
        return output

                



