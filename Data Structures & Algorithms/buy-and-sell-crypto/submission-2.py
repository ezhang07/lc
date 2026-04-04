class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0

        l = 0
        r = 1

        if len(prices) == 1:
            return 0
        
        while l < len(prices)-1:
            if r > len(prices)-1:
                l+=1
                r=l+1
                break
            if prices[r] < prices[l]:
                l = r
                r+=1
            else:
                res = max(res, prices[r]-prices[l])
                r+=1
        
        return res
            
            