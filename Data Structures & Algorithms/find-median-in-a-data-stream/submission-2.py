class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []
        
    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxHeap, -num)

        # every element in maxHeap <= every element in minHeap
        if self.minHeap and self.maxHeap and -self.maxHeap[0] > self.minHeap[0]:
            element = -heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, element)


        # checking that lengths dont differ by more than one
        if len(self.minHeap) > len(self.maxHeap) + 1:
            element = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -element)
        
        elif len(self.maxHeap) > len(self.minHeap) + 1:
            element = -heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, element)


    def findMedian(self) -> float:
        if len(self.minHeap) == len(self.maxHeap):
            return (self.minHeap[0] + -self.maxHeap[0]) / 2
        
        elif len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        
        else:
            return -self.maxHeap[0]
        
        