"""
https://leetcode-cn.com/problems/decode-ways/
"""

"""
解法一：动态规划
此题思想比较简单，但坑比较多
dp[i] 表示 前i个字符共有dp[i]个解码方式
边界条件：
    1. 如果第一个字符为0，直接返回0即可
    2. 边界：dp[0] = 1， 初始状态：dp[1] = 1.
状态转移方程：
    dp[i] = (dp[i-1] if s[i-1] != "0" else 0) 若当前字符不为0，则当前解码方式有效
            + (dp[i-2] if 9 < int(s[i-2:i]) < 27  else 0) 若与上一个字符（两个字符）构成了有效的解码方式，则解码方式有效
"""
class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        dp = [1,1]
        for i in range(2, len(s)+1):
            dp.append((dp[i-1] if s[i-1] != "0" else 0) + (dp[i-2] if 9 < int(s[i-2:i]) < 27  else 0))
        return dp[len(s)]


"""
递归法：
递归边界：
    1. 如果第一个字母为0，则返回0
    2. 如果字符长度为1或者0，则返回1
！递归法超出时间限制
"""
class Solution2:
    def numDecodings(self, s: str) -> int:
        if len(s) > 0 and s[0] == "0":
            return 0
        elif len(s) < 2:
            return 1
        return self.numDecodings(s[1:]) + (self.numDecodings(s[2:]) if 9<int(s[:2])<27 else 0)
s = Solution()
print(s.numDecodings("9371597631128776948387197132267188677349946742344217846154932859125134924241649584251978418763151253"))
        

