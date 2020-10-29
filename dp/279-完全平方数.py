class Solution:
    def numSquares(self, n: int) -> int:
        """
        dp[i]为正整数n所需要的完全平方数个数
        """
        dp = [i for i in range(0, n + 1)]
        for i in range(2, n + 1):
            j = 1
            while i - j * j > -1:
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1
        return dp[n]


s = Solution()
print(s.numSquares(0))
