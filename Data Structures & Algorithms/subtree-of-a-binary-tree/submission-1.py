# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
       
        def sameTree(tree_a, tree_b):
            if not tree_a and not tree_b:
                return True

            if not tree_a or not tree_b:
                return False

            if tree_a.val != tree_b.val:
                return False

            return sameTree(tree_a.left, tree_b.left) and sameTree(tree_a.right, tree_b.right)

        
        if root and not subRoot:
            return True

        if not root and not subRoot:
            return True

        if subRoot and not root:
            return False

        if root.val == subRoot.val:
            same = sameTree(root.left, subRoot.left) and sameTree(root.right, subRoot.right)

            if same:
                return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        