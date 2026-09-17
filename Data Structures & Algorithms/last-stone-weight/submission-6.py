class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []

        for stone in stones:
            heapq.heappush(heap, -stone)
        
        while len(heap) > 1:
            heaviest = -heapq.heappop(heap)
            second = -heapq.heappop(heap)

            if heaviest != second:
                heapq.heappush(heap, -(heaviest-second))
            
        if heap:
            return -heap[0]
        
        return 0
        