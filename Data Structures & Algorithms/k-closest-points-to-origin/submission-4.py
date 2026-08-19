class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        for point in points:
            distance = math.sqrt((point[0])**2 + (point[1])**2)
            maxHeap.append([-distance, point])

        heapq.heapify(maxHeap)

        while len(maxHeap) > k:
            heapq.heappop(maxHeap)

        result = []
        for element in maxHeap:
            result.append(element[1])
        
        return result