class TimeMap:
    def __init__(self):
        self.hmap = {}

    def set(self, key, value, timestamp):
        self.hmap[key] = self.hmap.get(key, [])
        self.hmap[key].append((timestamp, value))

    def get(self, key, timestamp):
        values = self.hmap.get(key, [])
        if not values:
            return ""

        left = 0
        right = len(values) - 1

        closest = float('-inf')
        closest_value = ""

        while left <= right:
            mid = (left + right) // 2
            ts = values[mid][0]
            value = values[mid][1]
            if ts <= timestamp:
                closest = ts
                closest_value = value
                left = mid + 1
            else:
                right = mid - 1

        return closest_value