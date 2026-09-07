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
            contribution = node.val if node.val > 0 else 0
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
    
            left = contributions[node.left] if node.left in contributions else 0
            right = contributions[node.right] if node.right in contributions else 0

            left = left if left > 0 else 0
            right = right if right > 0 else 0

            node_contribution = node.val

            global_max = max(global_max, node_contribution + left + right)

            contributions[node] = max(left, right) + node_contribution

            global_max = max(contributions[node], global_max)

        
        return global_max