# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        queue = [root]

        while queue:
            curr = queue.pop()

            if curr.val != root.val:
                return False
            
            if curr.left:
                queue.append(curr.left)

            if curr.right:
                queue.append(curr.right)

        return True