class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        res = nums[0]

        while l <= r:
            m = (l + r) // 2
            if nums[0] > nums[m]: # we are on the right side of the inflection point
                r = m - 1
                res = min(res, nums[m])

            else: # left side of inflection point
                l = m + 1
        
        return res