class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyIndex = prices.index(min(prices))
        sellIndex = prices.index(max(prices))

        # check the best day to buy which is minimum of array but it should not be last element
        # because we can't sell then 

        # check if buy is not last element
        while buyIndex == len(prices) - 1:
            prices.pop(buyIndex)
            if prices != []:
                buyIndex = prices.index(min(prices))
            else:
                return 0
        
        buy = prices[buyIndex]


        # we have to sell on which share price is highest but its index should be after buy index
        # because we cant sell before that

        # check if sell index if after the buy index
        while sellIndex < buyIndex:
            prices.pop(sellIndex)
            if prices != []:
                sellIndex = prices.index(max(prices))
            else:
                return 0

        ans = prices[sellIndex] - buy
        return ans


# optimized solution

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        ans = 0
        for i in range(1, len(prices)):
            if prices[i] < buy: # if price is less than buy then update buy to that price
                buy = prices[i] 
            else:
                ans = max(ans, prices[i] - buy) # else update ans to max of ans and price - buy
        return ans