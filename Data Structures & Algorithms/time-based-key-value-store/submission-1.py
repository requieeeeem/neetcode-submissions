class TimeMap:

    def __init__(self):
        self.dictionary = collections.defaultdict(list)
        
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dictionary[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        left = 0
        right = len(self.dictionary[key]) - 1

        prev_timestamp = -1
        while left <= right:
            mid = (left + right) // 2
            
            if self.dictionary[key][mid][1] <= timestamp:
                prev_timestamp = mid
                left = mid + 1
            else:
                right = mid - 1
        if prev_timestamp == -1:
            return ""
        return self.dictionary[key][prev_timestamp][0]