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
        if key not in self.map:
            return ""

        values = self.map[key]

        left, right = 0, len(values) - 1
        while left <= right:
            mid = left + (right - left) // 2

            curr = values[mid]

            if curr.timestamp == timestamp:
                return curr.value
            elif curr.timestamp > timestamp:
                right = mid - 1
            else: 
                left = mid + 1

        return values[right].value if values[right].timestamp <= timestamp else ""
        
