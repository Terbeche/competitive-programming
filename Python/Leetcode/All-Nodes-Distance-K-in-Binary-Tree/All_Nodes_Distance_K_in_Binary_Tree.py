# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if not root:
            return []

        graph = {}
        def build_graph(node, parent=None):
            if not node:
                return
            if node.val not in graph:
                graph[node.val] = []
            if parent:
                graph[node.val].append(parent.val)
                graph[parent.val].append(node.val)
            build_graph(node.left, node)
            build_graph(node.right, node)

        build_graph(root)

        queue = deque([(target.val, 0)])
        visited = set([target.val])
        answer = []

        while queue:
            node_val, distance = queue.popleft()
            if distance == k:
                answer.append(node_val)
            elif distance < k:
                for neighbor in graph[node_val]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, distance + 1))

        return answer