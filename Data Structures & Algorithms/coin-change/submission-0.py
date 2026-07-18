class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def solve(rem):
            if rem == 0:
                return 0
            if rem < 0:
                return float('inf')
            if rem in memo:
                return memo[rem]
            ans = float('inf')
            for coin in coins:
                ans = min(ans,1+solve(rem-coin))
            memo[rem] = ans
            return ans
        ans = solve(amount)
        return -1 if ans == float("inf") else ans