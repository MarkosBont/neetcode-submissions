import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]

        heapq.heapify(heap)

        while len(heap) > 1:
            heaviest = -heapq.heappop(heap)
            second_heaviest = -heapq.heappop(heap)

            if heaviest != second_heaviest:
                new_weight = heaviest - second_heaviest
                heapq.heappush(heap, -new_weight)
        
        if len(heap) == 0:
            return 0
        
        return -heap[0]