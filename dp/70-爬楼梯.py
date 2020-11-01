class Solution:
    
    def climbStairs1(self, n: int) -> int:
        # 1. 递归:超时
        if n<3:
            return n
        return self.climbStairs1(n-1)+self.climbStairs1(n-2)

    def climbStairs(self, n: int) -> int:
        if n<3:
            return n
        # 2. 动态规划
        dp = [0] * (n+1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

s = Solution()
print(s.climbStairs(44))