class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        buy = 0
        sell = 1
        result = 0

        while sell < len(prices):
            
            if prices[buy] > prices[sell]:
                buy = sell
            
            else:
                profit = prices[sell] - prices[buy]
                result = max(result, profit)
            
            sell += 1
        
        return result


