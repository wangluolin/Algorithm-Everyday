"""
https://leetcode-cn.com/problems/wildcard-matching/
通配符匹配
"""

"""
方法一：递归法
Error： 超出时间限制
"""


class Solution1:
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s
        if not s:
            return p[0] == '*' and self.isMatch(s, p[1:])  # 出现多个*号匹配空格
        if p[0] == '*':
            return self.isMatch(s[1:], p) or self.isMatch(s, p[1:])
        elif p[0] == '?':
            return self.isMatch(s[1:], p[1:])
        else:
            return s[0] == p[0] and self.isMatch(s[1:], p[1:])


"""
方法二：动态规划
bool dp[len(p)+1][len(s)+1]表示不同位置的模式p对不同位置的匹配情况
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[1] * (len(s) + 1) for i in range(len(p) + 1)]  # dp[len(p)+1][len(s)+1]
        for i in range(1, len(s) + 1):
            dp[0][i] = 0  # 如果p的长度为0，则dp一定为false
        for i in range(1, len(p) + 1):
            dp[i][0] = (p[i - 1] == '*' and dp[i - 1][0] == 1)  # 如果s的长度为0
        for i in range(1, len(p) + 1):
            for j in range(1, len(s) + 1):
                dp[i][j] = (dp[i - 1][j - 1] and (p[i - 1] == '*' or p[i - 1] == '?' or s[j - 1] == p[i - 1])) or \
                           ((dp[i - 1][j] or dp[i][j - 1]) and p[i - 1] == '*')  # 单个字符匹配 or *号匹配多个字符

        # print(dp)
        return dp[len(p)][len(s)]


s = Solution()
print(s.isMatch("aa", "a***"))
