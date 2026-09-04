# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        if not root:
            return None

        curr_val = root.val
       
        
        if p.val < curr_val and q.val < curr_val:
            return self.lowestCommonAncestor(root.left, p, q)

        if p.val > curr_val and q.val > curr_val:
            return self.lowestCommonAncestor(root.right, p , q)

        # LCA when there is a split is the root itself
        return root

