class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = defaultdict(int)
        freq = [[] for i in range(len(nums)+1)]

        for num in nums:
            hmap[num] += 1

        for n, f in hmap.items():
            freq[f].append(n)
        
        output = []
        for i in range(len(freq)-1, 0, -1):
            for j in freq[i]:
                output.append(j)
                if len(output) == k:
                    return output
        