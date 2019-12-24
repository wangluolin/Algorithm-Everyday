"""
https://leetcode-cn.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
根据中序和后序还原二叉树
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

"""
思路一：递归
自上向下构建二叉树
"""
class Solution:
    def buildTree(self, inorder, postorder) -> TreeNode:
        # 一定要注意递归边界！
        if not inorder or not postorder: return None
        root = TreeNode(postorder[-1])
        idx = inorder.index(root.val)
        root.left = self.buildTree(inorder[:idx], postorder[:idx])
        root.right = self.buildTree(inorder[idx+1:], postorder[idx:-1])
        return root



if __name__ == "__main__":
    s = [1,2,2,4]
    print(s[-1])


#     2
#  5       7
# 4 6    9  10

# inOrder: 4 5 6 2 9 7 10
# post   : 4 6 5 9 10 7 2