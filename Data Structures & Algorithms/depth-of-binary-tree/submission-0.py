# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        

        def dfs(node, current):
            if not node:
                return current

            left = dfs(node.left, current + 1)
            right = dfs(node.right, current + 1)

            return max(left, right)

        return dfs(root, 0)