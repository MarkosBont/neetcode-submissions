import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []

        heapq.heapify(maxHeap)

        for point in points:
            x, y = point
            distance = math.sqrt((x)**2 + (y)**2)
            distance_point = (-distance, point)

            heapq.heappush(maxHeap, distance_point)

            if len(maxHeap) > k:
                heapq.heappop(maxHeap)


        return [distance_point[1] for distance_point in maxHeap]