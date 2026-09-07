# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = root.val

        def dfs(root):
            nonlocal result

            if not root:
                return 0

            left_max = max(dfs(root.left), 0)
            right_max = max(dfs(root.right), 0)

            result = max(result, root.val + left_max + right_max)

            return root.val + max(left_max, right_max)

        dfs(root)

        return result

