class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, currentProfit, maxProfit = 0, 0, 0

        for right in range(len(prices)):
            if prices[right] > prices[left]:
                currentProfit = prices[right] - prices[left]
                maxProfit = max(maxProfit, currentProfit)
            else: #loert price was found, so buy day got moved
                left=right
        return maxProfit

            