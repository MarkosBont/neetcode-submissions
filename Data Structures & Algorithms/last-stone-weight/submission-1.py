import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = []
        for stone in stones:
            heapq.heappush(maxHeap, -stone)
        
        while len(maxHeap) > 1:
            heaviest = -heapq.heappop(maxHeap)
            second_heaviest = -heapq.heappop(maxHeap)

            if heaviest != second_heaviest:
                heapq.heappush(maxHeap, -(heaviest - second_heaviest))
            
        return -maxHeap[0] if maxHeap else 0



        