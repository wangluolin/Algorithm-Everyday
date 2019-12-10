"""
https://leetcode-cn.com/problems/validate-binary-search-tree/
98. 验证合法的二叉搜索树
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

"""
方法一：中序遍历的方式
1. 注意题目，节点间严格大于小于，所以在排序时要转换为set进行判断
2. 列表之间可用+来连接
"""
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        arr = self.inOrderTra(root)
        return arr == sorted(set(arr)) # set的作用是避免重复值出现
    def inOrderTra(self, root: TreeNode):
        if not root:
            return []
        return self.inOrderTra(root.left)+[root.val]+self.inOrderTra(root.right) # 列表之间可用+号来连接

"""
方法二：边界法
1. 每个节点都具有边界值，递归即可
2. python3中获取最大值的方法是sys.maxsize
"""
import sys
class Solution2:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.isValidBoundary(root)
    def isValidBoundary(self, root: TreeNode, b_min=-sys.maxsize, b_max=sys.maxsize) -> bool:
        if not root:
            return True
        if b_min < root.val < b_max:
            return self.isValidBoundary(root.left, b_min, root.val) and \
                self.isValidBoundary(root.right, root.val, b_max)
        else:
            return False

if __name__ == "__main__":
    pass
    
