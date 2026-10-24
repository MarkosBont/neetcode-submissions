class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return []
        
        hmap = {}
        for num in nums:
            hmap[num] = hmap.get(num, 0) + 1


        arr = [[] for _ in range(len(nums)+1)] 
        
        for key, val in hmap.items():
            arr[val].append(key)
        
        final = []

        for i in range(len(arr)-1, -1, -1):
            for item in arr[i]:	
                final.append(item)
                if len(final) == k:
                    return final