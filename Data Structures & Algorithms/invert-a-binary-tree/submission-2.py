# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        queue = [root]

        while queue:
            node = queue.pop()

            left = node.left
            right = node.right

            node.left = right
            node.right = left
            if right:
                queue.append(right)
            if left:
                queue.append(left)

        return root