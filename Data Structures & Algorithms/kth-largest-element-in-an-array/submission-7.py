class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = []
        heapq.heapify(maxHeap)

        for num in nums:
            heapq.heappush(maxHeap, -num)
        
        while len(maxHeap) > len(nums)-k+1:
            heapq.heappop(maxHeap)
        
        return -maxHeap[0]
        
        