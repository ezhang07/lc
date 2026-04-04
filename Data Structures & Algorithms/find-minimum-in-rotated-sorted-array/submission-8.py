class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        res = nums[0]

        if nums[0] <= nums[-1]:
            return res

        while l <= r:
            m = (l+r)//2
            res = min(res, nums[m])
            if nums[0] <= nums[m]:
                l = m + 1

            else:
                r = m - 1

        
        return res
