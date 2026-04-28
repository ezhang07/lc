class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucketSort = [[] for _ in range(len(nums) + 1)]
        freqTable = {}

        for n in nums:
            freqTable[n] = freqTable.get(n, 0) + 1
        
        for key, v in freqTable.items():
            bucketSort[v].append(key)

        res = []

        for i in range(len(bucketSort)-1, 0, -1):
            for v in bucketSort[i]:
                res.append(v)
                if len(res) == k:
                    return res
                 
        return res