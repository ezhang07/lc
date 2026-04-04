class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        starters = defaultdict(set)
        nums = set(nums)
        maxlen = 0

        for n in nums:
            if (n-1) not in nums:
                starters[n].add(n)

        for n in starters:
            i = n
            length = 1
            if length > maxlen:
                maxlen = length
            while (i+1) in nums:
                starters[n].add(i+1)
                i+=1
                length+=1
                if length > maxlen:
                    maxlen = length
        
        return maxlen

        

            