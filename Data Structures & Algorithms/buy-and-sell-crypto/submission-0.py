class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_min,mini = float('inf'),0
        curr_max,maxi = 0,0
        profit = 0
        for i in range(len(prices)):
            if prices[i] < curr_min:
                curr_min = prices[i]
                curr_max = 0
                maxi = 0
                mini = i
            if prices[i] > curr_max:
                curr_max = prices[i]
                maxi = i
            if mini < maxi:
                profit = max(profit,curr_max-curr_min)
        return profit


        