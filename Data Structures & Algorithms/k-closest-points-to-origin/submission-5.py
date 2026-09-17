class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = []
        distance_points = [] # holds tuples of form (distance, point)
        output = []

        for point in points:
            distance_to_origin = math.sqrt(point[0]**2 + point[1]**2)
            tup = (-distance_to_origin, point)
            heapq.heappush(minheap, tup)
        
        while len(minheap) > k:
            heapq.heappop(minheap)
        
        points = [x[1] for x in minheap]
        return points

        