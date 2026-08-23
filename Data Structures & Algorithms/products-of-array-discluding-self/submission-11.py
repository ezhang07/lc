class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [1] * len(nums)
        prefixProd = 1
        suffixProd = 1

        for i in range(1, len(nums)):
            prefixProd *= nums[i - 1]
            res[i] *= prefixProd
        
        for i in range(len(nums) - 2, -1, -1):
            suffixProd *= nums[i + 1]
            res[i] *= suffixProd
        
        return res


            