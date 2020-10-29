class Solution:
    def minCostClimbingStairs(self, cost) -> int:
        """
        dp[i]表示登上第i个阶梯所花费的体力值。
        登上楼顶所花费的体力值为0，
        所以我们要登上n层阶梯的阶梯顶部，则要求dp[n+1]
        """
        n = len(cost)
        if n < 1:
            return 0
        dp = [0] * (n+1)
        cost.append(0)
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, n+1):
            dp[i] = min(dp[i-1], dp[i-2]) + cost[i]

        return dp[n]


s = Solution()
print(s.minCostClimbingStairs([]))
