import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k
        heapq.heapify(self.heap)

        for i, num in enumerate(nums):
            if len(self.heap) < k:
                heapq.heappush(self.heap, num)
            else:
                smallest = self.heap[0]
                if num > smallest:
                    heapq.heappop(self.heap)
                    heapq.heappush(self.heap, num)

        
    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)

        else:
            smallest = self.heap[0]
            if val > smallest:
                heapq.heappop(self.heap)
                heapq.heappush(self.heap, val)

        return self.heap[0]