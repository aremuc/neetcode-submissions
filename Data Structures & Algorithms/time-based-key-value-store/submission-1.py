class TimeMap:

    def __init__(self):
        self.store = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        
        if key not in self.store:
            self.store[key] = []
            
        self.store[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        
        if key not in self.store:
            return ''

        start = 0
        end = len(self.store[key]) - 1
        result = ''

        while start <= end:

            mid = (start + end) // 2

            if self.store[key][mid][1] == timestamp:
                return self.store[key][mid][0]

            elif self.store[key][mid][1] > timestamp:
                end = mid -1

            else:
                result = self.store[key][mid][0]
                start = mid + 1
        
        return result
