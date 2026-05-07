# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=self.levelOrder(root)
        res.reverse()

        return res


    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:  return []
        res, queue = [], [root]

        while queue:
            levelQueue = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                levelQueue.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)   
            res.append(levelQueue)
        
        return res