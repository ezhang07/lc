class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        keyList = self.timeMap[key]
        n = len(keyList)
        l = 0
        r = n - 1
        res = ""

        while l <= r:
            m = (l+r)//2

            if keyList[m][1] > timestamp:
                r = m - 1
            elif keyList[m][1] < timestamp:
                res = keyList[m][0]
                l = m + 1
            else:
                return keyList[m][0]
        

        
        return res
