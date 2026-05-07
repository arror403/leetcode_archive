# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        t=self.levelOrder(root)
        # print(len(t))
        for i in range(len(t)):
            if i%2==1:
                # print(t[i])
                t[i].reverse()
        # print(t)
        return t


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