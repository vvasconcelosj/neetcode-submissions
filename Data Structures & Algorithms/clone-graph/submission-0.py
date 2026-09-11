"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        old_to_new = {}

        queue = deque([node])

        while queue:
            for i in range(len(queue)):
                curr = queue.popleft()
                if curr not in old_to_new:
                    old_to_new[curr] = Node(curr.val)

                new = old_to_new[curr]
                for neighbor in curr.neighbors:
                    if neighbor not in old_to_new:
                        queue.append(neighbor)
                        old_to_new[neighbor] = Node(neighbor.val)

                    new_neightbor = old_to_new[neighbor]
                    new.neighbors.append(new_neightbor)

        return old_to_new[node]

                