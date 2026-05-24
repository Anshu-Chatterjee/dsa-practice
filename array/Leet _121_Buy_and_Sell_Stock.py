# Problem: Best Time to Buy and Sell Stock (#121)
# Difficulty: Easy
# Pattern: Greedy / Single Pass
# Time: O(n) | Space: O(1)


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0           # first we initialize profit to 0 and buy to the first price in the list.
        buy=prices[0]
        for i in prices:   #  Then we iterate through each price in the list.
            buy=min(buy,i)  # updating the buy variable to be the minimum of the current buy and the current price.
            profit=max(profit,i-buy) #  We also update the profit variable to be the maximum of the current profit and the difference between the current price and the buy price.
        return profit                 #  Finally, we return the profit variable, which will contain the maximum profit that can be achieved from buying and selling a stock.  





