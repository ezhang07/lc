class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        freqMap = {} # value : frequency

        # build freqMap
        for i, n in enumerate(nums):
            freqMap[n] = freqMap.get(n, 0) + 1
        
        bucketSort = [[] for _ in range(len(nums) + 1)]

        for val, freq in freqMap.items():
            bucketSort[freq].append(val) # consider multiple vals with same freq
        

        res = []
        for i in range(len(nums), -1, -1):
            if k == 0:
                return res
            for n in bucketSort[i]:
                res.append(n)
                k-=1

        return res