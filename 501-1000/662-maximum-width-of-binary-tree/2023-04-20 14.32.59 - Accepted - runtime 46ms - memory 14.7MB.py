# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        max_width = 0
        queue = [(root, 0)]

        while queue:
            level_size = len(queue)
            _, level_start = queue[0]
            for i in range(level_size):
                node, col_idx = queue.pop(0)
                if node.left:
                    queue.append((node.left, 2 * col_idx))
                if node.right:
                    queue.append((node.right, 2 * col_idx + 1))
            max_width = max(max_width, col_idx - level_start + 1)

        return max_width