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
                new_stone = heaviest - second_heaviest
                heapq.heappush(maxHeap, -new_stone)
        

        if len(maxHeap) == 1:
            return -maxHeap[0]
        
        else:
            return 0



        