"""
97. Interleaving String
https://leetcode-cn.com/problems/interleaving-string/
"""

"""
动态规划
dp[i,j]表示s1[:i]和s2[:j]是否能交错形成s3[:i+j]
边界条件：
    1. 长度不相等直接返回FALSE
    2. 边界值为是否和s3匹配
状态转移方程：
    根据上一次的匹配字符，判断本次是否匹配
    dp[i][j] = 1 if (dp[i-1][j] == 1 and s1[i-1]==s3[i+j-1]) else 0 
    dp[i][j] = 1 if (dp[i][j-1] == 1 and s2[j-1]==s3[i+j-1]) else 0
"""
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        
        dp = [[0]*(1+len(s2)) for _ in range(1+len(s1))]
        dp[0][0] = 1
        for i in range(1, len(s1)+1):
            dp[i][0] = 1 if (dp[i-1][0]==1 and s1[i-1]==s3[i-1]) else 0
        for i in range(1, len(s2)+1):
            dp[0][i] = 1 if (dp[0][i-1]==1 and s2[i-1]==s3[i-1]) else 0
        
        for i in range(1, len(s1)+1):
            for j in range(1, len(s2)+1):
                dp[i][j] = 1 if (dp[i-1][j] == 1 and s1[i-1]==s3[i+j-1]) else 0
                if dp[i][j] == 0:
                    dp[i][j] = 1 if (dp[i][j-1] == 1 and s2[j-1]==s3[i+j-1]) else 0
        return dp[len(s1)][len(s2)]

s = Solution()
s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbbaccc"
print(s.isInterleave(s1, s2, s3))