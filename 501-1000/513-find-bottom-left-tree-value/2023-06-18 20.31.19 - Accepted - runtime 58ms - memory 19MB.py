# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        # Check if the tree is empty
        if not root:
            return None

        queue = deque([root])
        leftmost_value = None

        while queue:
            level_size = len(queue)

            # Process all nodes at the current level
            for i in range(level_size):
                node = queue.popleft()

                # Update the leftmost value for the first node in the level
                if i == 0:
                    leftmost_value = node.val

                # Add the children of the current node to the queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return leftmost_value