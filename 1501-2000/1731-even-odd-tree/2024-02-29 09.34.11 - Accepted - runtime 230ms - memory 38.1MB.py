class Solution:
    
    ##### power by chatGPT #####

    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        queue = deque([root])
        level = 0  # Use level to determine even or odd level

        while queue:
            prev_val = None  # To store the previous node value in the current level
            level_size = len(queue)

            for _ in range(level_size):
                node = queue.popleft()

                # Check if the current node value violates the rules
                if (level % 2 == 0 and (node.val % 2 == 0 or (prev_val is not None and prev_val >= node.val))) or \
                   (level % 2 == 1 and (node.val % 2 == 1 or (prev_val is not None and prev_val <= node.val))):
                    return False

                prev_val = node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            level += 1  # Move to the next level

        return True
