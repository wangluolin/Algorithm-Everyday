# 最长圆括号匹配
# https://leetcode-cn.com/problems/longest-valid-parentheses/

class Solution:
    # 第一种解法
    def longestValidParentheses(self, s: str) -> int:
        """
        1. 将每个合理的括号标为1
            a. 将每个(的位置加入栈
            b. 如果)出现时，栈不为空，则栈顶取出位置和当前位置设为1
        2. 寻找连续1的最大长度
        """
        p, sk = [0]*len(s), []
        for i, c in enumerate(s):
            if c == '(':
                sk.append(i)
            elif c == ')' and len(sk) > 0:
                p[sk.pop()] = 1
                p[i] = 1
        tmp, result = 0, 0

        for i in p:
            if i == 1:
                tmp += 1
                result = max(result, tmp)
            else:
                tmp = 0
        return result
    
    # 第二种解法
    def longestValidParentheses2(self, s: str) -> int:
        """
        1. 从左检索有效括号长度，当左括号等于右括号时，记录长度
        2. 从右向左重复检索，避免出现()(()()这样的情况，导致误判
        """
        result, curLen, tmp = 0, 0, 0
        for i in s:
            curLen += 1
            tmp += 1 if i == '(' else -1
            if tmp == 0:
                result = max(result, curLen)
            elif tmp < 0:
                curLen = 0
                tmp = 0
        curLen, tmp = 0, 0
        for i in range(len(s)-1, -1, -1):
            curLen += 1
            tmp += 1 if s[i] == ')' else -1
            if tmp == 0:
                result = max(result, curLen)
            elif tmp < 0:
                curLen = 0
                tmp = 0
        return result
    
    # 第三种解法
    def longestValidParentheses3(self, s: str) -> int:
        """
        动态规划解法
        1. 如果s[i]==')'，且s[i-1]=='('，则dp[i] = 2+dp[i-2]
        2. 如果s[i]==')'，且s[i-1]==')'，且s[i-dp[i-1]-1]=='('，则dp[i] = dp[i-1]+dp[i-dp[i-1]-2]+2
        """
        result, dp = 0, [0] * len(s)
        
        for i in range(1,len(s)):
            if s[i]==')' and s[i-1] == '(':
                dp[i] = dp[i-2] + 2 if i>1 else 2
            elif s[i] == ')' and s[i-1] == ')'and i-dp[i-1]-1>=0  and s[i-dp[i-1]-1] == '(':
                dp[i] = dp[i-1] + dp[i-dp[i-1]-2] + 2 if i-dp[i-1]-2>=0 else dp[i-1]+2
            result = max(result, dp[i])
        return result

su = Solution()
print(su.longestValidParentheses3("(())"))



            

