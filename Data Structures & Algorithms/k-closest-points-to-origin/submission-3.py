class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []

        for point in points:
            d_origin = math.sqrt((point[0])**2 + (point[1])**2)
            distances.append([d_origin, point])

        heapq.heapify(distances)

        result = []
        while len(result) < k:
            close_point = heapq.heappop(distances)
            result.append(close_point[1])
        
        return result
        

        