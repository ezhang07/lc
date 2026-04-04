class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0

        numSet = set(nums)
        seqMap = defaultdict(list)
        maxSeq = 1

        for n in numSet:
            curSeq = 1
            if n-1 not in numSet: 
                nextNum = n+1
                while nextNum in numSet:
                    curSeq+=1
                    maxSeq=max(maxSeq,curSeq)
                    nextNum+=1

            if n-1 in numSet:
                continue
        
        return maxSeq
            