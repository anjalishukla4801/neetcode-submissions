class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=0
        min_price=prices[0]
        for i in prices[1:]:
            if i<min_price:
                min_price=i
            max_profit=max(i-min_price,max_profit)
        return max_profit    
        