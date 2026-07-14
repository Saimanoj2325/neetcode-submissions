class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        #Base case 1
        for i in range(n):
            dp[i][i] = True
        maxi = 1
        start = 0
        for l in range(2,n+1):
            for i in range(n-l+1):
                j = i+l-1
                if s[i] == s[j]:
                    if l == 2 or dp[i+1][j-1]:
                        dp[i][j] = True
                        if l > maxi:
                            maxi = l
                            start = i
        return s[start:start+maxi]

                    