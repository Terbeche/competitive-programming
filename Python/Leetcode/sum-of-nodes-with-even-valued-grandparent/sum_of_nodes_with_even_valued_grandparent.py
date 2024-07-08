# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        answer = 0
        queue = deque([(root, None, None)])
        level = 0

        while queue:
            node, grandparent, parent = queue.popleft()

            if grandparent and grandparent.val % 2 == 0:
                answer += node.val

            if node.left:
                queue.append((node.left, parent, node))
            if node.right:
                queue.append((node.right, parent, node))

        return answer
