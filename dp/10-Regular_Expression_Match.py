"""
https://leetcode-cn.com/problems/regular-expression-matching/submissions/
思路：递归法
2. 如果p[0] == {s[0], '.'}, 则递归p[1:], s[1:]
1. 如果len(p) >= 2, p[1] == '*'则：
    A. 递归p[2:], s， 则表示p和前面的字符未匹配
    B. 递归p, s[1:]，则表示*匹配了一次，进行*的下一次匹配
"""
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p: 
            return not s
        first_match = bool(s) and p[0] in {s[0], '.'} # bool(s) means s not null
        if len(p) >1 and p[1] == '*':
            return (self.isMatch(s, p[2:])) or (first_match and self.isMatch(s[1:], p))
        else:
            return self.isMatch(s[1:], p[1:]) and first_match

s = Solution()
print(s.isMatch("aab", "c*a*b"))


