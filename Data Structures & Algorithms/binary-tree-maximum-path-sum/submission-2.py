# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        # Post order traversal
        # Store the node and their contribution so far
        stack1 = [root]
        stack2 = []

        while stack1:
            node = stack1.pop()
            stack2.append(node)

            if node.left:
                stack1.append(node.left)

            if node.right:
                stack1.append(node.right)

        # Key: node, value: contribution to parent
        contributions = {}
        global_max = float('-inf')

        while stack2:
            node = stack2.pop()
    
            left = contributions.get(node.left, 0)
            right = contributions.get(node.right, 0)

            left = max(left, 0)
            right = max(right, 0)



            global_max = max(global_max, node.val + left + right)
            contributions[node] = node.val + max(left, right)


        
        return global_max