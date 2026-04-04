class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixProd = 1
        suffixProd = 1
        res = [1]*len(nums)

        for i in range(len(nums)-1):
            prefixProd*=nums[i]
            res[i+1] = prefixProd
        
        for i in range(len(nums)-1, 0, -1):
            suffixProd*=nums[i]
            res[i-1]*=suffixProd
        

        return res
