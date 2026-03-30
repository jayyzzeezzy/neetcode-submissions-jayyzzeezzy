# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxD = 0

        def dfs(root):
            nonlocal maxD

            if not root: return 0

            maxD = max(maxD, dfs(root.left) + dfs(root.right))
            return 1 + max(dfs(root.left), dfs(root.right))

        dfs(root)
        return maxD