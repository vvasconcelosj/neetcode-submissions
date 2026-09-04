# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def validateNode(self, node: Optional[TreeNode], upper: int, lower: int) -> bool:
        if not node:
            return True

        if node.val >= upper or node.val <= lower:
            return False

        return self.validateNode(node.left, node.val, lower) and self.validateNode(node.right, upper, node.val)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        return self.validateNode(root, float('inf'), float('-inf'))
    