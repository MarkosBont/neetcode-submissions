class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []

        hmap = {}
        l = [[] for i in range(len(nums)+1)]
        output = []

        for num in nums:
            hmap[num] = hmap.get(num, 0) + 1
        
        for num, freq in hmap.items():
            l[freq].append(num)
        
        for i in range(len(nums), -1, -1):
                for num in l[i]:
                    output.append(num)
                    k -= 1
                    if k == 0:
                        return output



        


        