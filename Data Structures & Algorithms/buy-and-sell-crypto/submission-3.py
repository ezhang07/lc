class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        :type prices: List[int]
        :rtype: int
        edge case: len == 1, return 0

        7, 1, 5, 3, 6, 4
        """

        profit = 0

        if len(prices) == 1:
            return profit
        
        l, r = 0, 1

        while r < len(prices):
            if prices[l] > prices[r]: # right pointer smaller, no profit, move left pointer to right, right pointer + 1
                l = r
                r = l + 1
            else: # right pointer larger than left pointer, so just wanna see if it's bigger than the max we've seen, and move right
                profit = max(profit, prices[r] - prices[l])
                r += 1
        
        return profit
            