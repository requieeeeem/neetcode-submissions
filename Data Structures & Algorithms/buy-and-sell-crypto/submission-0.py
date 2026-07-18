class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0 #used to track buying
        right = 1 #used to track selling
        maxProfit = 0
        
        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                if profit > maxProfit:
                    maxProfit = profit
                right += 1
            else:
                left = right
                right += 1
        return maxProfit