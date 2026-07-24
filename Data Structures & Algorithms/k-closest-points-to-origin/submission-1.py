class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []

        for point in points:
            d_origin = math.sqrt((point[0])**2 + (point[1])**2)
            distances.append([d_origin, point])

        heapq.heapify(distances)

        result = [heapq.heappop(distances)[1] for _ in range(k)]

        return result
        

        