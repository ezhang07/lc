class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 0:
            return 0

        sequence = set(nums)
        res = 1

        for n in sequence:
            if n - 1 not in sequence:
                count = 1
                while n + count in sequence:
                    count += 1
                    res = max(res, count)
            
        return res
        
        