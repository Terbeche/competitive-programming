class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        has_parent = set(leftChild + rightChild)
        has_parent.discard(-1)

        if len(has_parent) == n:
            return False

        node = root = 0
        visited = set()

        for node in range(n):
            if node not in has_parent:
                root = node
                break

        def dfs(node):
            if node == -1:
                return True
            if node in visited:
                return False
            
            visited.add(node)

            return dfs(leftChild[node]) and dfs(rightChild[node])
        
        return dfs(root) and len(visited) == n