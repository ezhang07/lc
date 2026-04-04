class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix = []
        suffix = []
        prefixProd = 1
        suffixProd = 1

        for n in nums:
            prefixProd*=n
            prefix.append(prefixProd)

        for n in reversed(nums):
            suffixProd*=n
            suffix.append(suffixProd)
        suffix = list(reversed(suffix))

        res = []
       


        for i, n in enumerate(nums):
            if i == 0:
                prod = suffix[i+1]
                res.append(prod)
                continue

            if i == len(nums)-1:
                prod = prefix[i-1]
                res.append(prod)
                continue
            
            prod = prefix[i-1]*suffix[i+1]
            res.append(prod)
            
        return res
            
                