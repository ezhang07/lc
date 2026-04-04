class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
            
        curSeq = 1
        maxSeq = 1
        dupe = set(nums)
        sortedNums = sorted(list(dupe))

        for i in range(1, (len(sortedNums))):
            if sortedNums[i] - 1 == sortedNums[i-1]:
                curSeq+=1
                maxSeq = max(curSeq,maxSeq)
            else:
                curSeq=1
        
        return maxSeq
                


        

