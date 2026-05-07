# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        q_original = deque([original])
        q_cloned = deque([cloned])

        # The loop continues as long as there are nodes to process.
        while q_original:
            # Dequeue one node from each tree. They will always correspond to each other.
            node_original = q_original.popleft()
            node_cloned = q_cloned.popleft()

            # If the node from the original tree is the target we're looking for...
            if node_original == target:
                # ...then the corresponding node from the cloned tree is our answer.
                return node_cloned

            # Enqueue the children for the next level of traversal, if they exist.
            # We must do this for both trees to keep them in sync.
            if node_original.left:
                q_original.append(node_original.left)
                q_cloned.append(node_cloned.left)
            
            if node_original.right:
                q_original.append(node_original.right)
                q_cloned.append(node_cloned.right)