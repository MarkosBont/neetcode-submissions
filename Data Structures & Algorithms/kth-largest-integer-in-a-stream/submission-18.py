class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k
        
        if self.k < len(nums):
            for i in range(k):
                heapq.heappush(self.heap, nums[i])
            
            for i in range(k, len(nums)):
                heapq.heappop(self.heap)
                heapq.heappush(self.heap, nums[i])
        
        else:
            for i in range(len(nums)):
                heapq.heappush(self.heap, nums[i])


    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        
        else:
            heapq.heappop(self.heap)
            heapq.heappush(self.heap, val)

        return self.heap[0]
        
