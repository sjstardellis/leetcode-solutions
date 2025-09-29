from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # initialize first day
        buy = prices[0]
        # profit tracker
        profit = 0

        # go through from 1-n, not 0
        for i in range(1, len(prices)):
            # if the price at the current index is less than the buy
            if prices[i] < buy:
                # update buy
                buy = prices[i]
            # if the price-buy (profit) is greater than the current profit
            elif prices[i]-buy > profit:
                # set new profit total
                profit = prices[i] - buy
        return profit