class TimeValue:
    def __init__(self, value: str, timestamp: int):
        self.value = value
        self.timestamp = timestamp

class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        val = TimeValue(value, timestamp)
        self.map[key].append(val)
        

    def get(self, key: str, timestamp: int) -> str:
        res = ""

        values = self.map.get(key, [])
        left, right = 0, len(values) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if values[mid].timestamp <= timestamp:
                res = values[mid].value
                left = mid + 1
            else:
                right = mid - 1

        return res
        
