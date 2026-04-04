class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        l = 0
        r = 1

        # some for loop/while loop
        # if prices[r] < prices[l]:
        # l = r and r +=1?
        # else: profit = prices[r]-prices[l] r+=1
        profit = 0
        

        for i in range(len(prices)-1):
            for j in range(i+1,len(prices)):
                if (prices[j]-prices[i]) > profit:
                    profit = prices[j]-prices[i]
        return profit