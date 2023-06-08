class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if sorted(prices, reverse=True) == prices:
            return 0
        
        buy_price = prices[0]
        sell_price = 0
        
        for num, p in enumerate(prices):
            
            if p < buy_price:
                buy_price = p
                # print("b", buy_price)
            
            # elif p > total + buy_price:
            elif p > buy_price + sell_price:

                sell_price = p - buy_price
                # print("s", sell_price)
                
        return sell_price
        