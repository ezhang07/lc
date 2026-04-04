class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        suffix = [1]
        prefixProd = 1
        suffixProd = 1
        res = [0]*len(nums)

        for i in range(len(nums)-1):
            prefixProd*=nums[i]
            prefix.append(prefixProd)
        
        for i in range(len(nums)-1, 0, -1):
            suffixProd*=nums[i]
            suffix.append(suffixProd)
        
        suffix.reverse()

        for i in range(len(nums)):
            res[i]=prefix[i]*suffix[i]

        return res
