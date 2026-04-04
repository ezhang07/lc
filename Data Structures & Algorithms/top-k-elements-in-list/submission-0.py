class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqTable = {} # value: frequency
        bucketSort = [[] for i in range(len(nums)+1)]
    

        for n in nums:
            freqTable[n]= 1+freqTable.get(n,0)

        for val, freq in freqTable.items():
            bucketSort[freq].append(val)
        
        res = []

        for i in range(len(bucketSort)-1, 0,-1):
            if k==0:
                return res
            for num in bucketSort[i]:
                res.append(num)
                k-=1
            
        
        return res


        