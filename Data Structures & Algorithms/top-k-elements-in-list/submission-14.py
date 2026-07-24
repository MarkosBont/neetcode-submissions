class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}
        output = []

        for num in nums:
            hmap[num] = hmap.get(num, 0) + 1
        
        freq_array = [[] for i in range(len(nums) + 1)]

        for num, freq in hmap.items():
            freq_array[freq].append(num)
        

        for i in range(len(nums), -1, -1):
            if len(freq_array[i]) != 0:
                for num in freq_array[i]:
                    output.append(num)
                    k -= 1
            
            if k == 0:
                return output

            
            



            

            

        