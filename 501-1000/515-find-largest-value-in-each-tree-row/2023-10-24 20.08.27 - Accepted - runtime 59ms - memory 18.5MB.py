# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        return [] if not self.LevelOrder(root) else [max(i) for i in self.LevelOrder(root)]

    def LevelOrder(self, root):
        if not root: return None
            
        q = [root]
        res = []

        while q:
            row = []
            l = len(q)
            for i in range(l):
                curr = q.pop(0)
                row.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            res.append(row)
            
        return res