class Solution:
    ##### power by perplexity #####
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:     
        if depth == 1:
            return TreeNode(val, root, None)

        queue = deque([(root, 1)])
        while queue:
            node, level = queue.popleft()
            if level == depth - 1:
                node.left = TreeNode(val, node.left, None)
                node.right = TreeNode(val, None, node.right)
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))

        return root