class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        INF = float("inf")
        dp = [INF]*(amount+1)
        dp[0] = 0
        for rem in range(1,amount+1):
            for coin in coins:
                if rem >= coin:
                    dp[rem] = min(dp[rem],1+dp[rem-coin])
        return -1 if dp[amount] == INF else dp[amount]