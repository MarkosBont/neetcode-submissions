class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-stone for stone in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            heaviest = -heapq.heappop(maxHeap)
            heaviest2 = -heapq.heappop(maxHeap)

            if heaviest > heaviest2:
                heapq.heappush(maxHeap, -(heaviest-heaviest2))
        
        if maxHeap:
            return -maxHeap[0]

        else:
            return 0

        