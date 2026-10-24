class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []

        for i in range(k):
            heapq.heappush(self.heap, nums[i])

        for i in range(k, len(nums)):
            heapq.heappop(self.heap)
            heapq.heappush(self.heap, nums[i])

    def add(self, val: int) -> int:
        heapq.heappop(self.heap)
        heapq.heappush(self.heap, val)

        return self.heap[0]
        
